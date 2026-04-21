# -*- coding: utf-8 -*-
"""
GIS Quy Hoạch AI Chat Backend — Claude-powered tư vấn viên GIS
Chạy: python chat_backend.py
API: POST http://localhost:8000/chat

🔐 Bảo mật:
  - Rate limiting: 15 request/phút mỗi IP
  - CORS chỉ cho phép domain trong ALLOWED_ORIGINS
  - Input validation: max 2000 ký tự/tin, max 20 tin/lượt, role phải hợp lệ
  - API key không hardcode — load từ .env
"""
import os
import csv
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import List
import anthropic
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

load_dotenv()

# ── Cấu hình ──────────────────────────────────────────────────────
CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
MODEL = "claude-haiku-4-5"   # Nhanh + rẻ nhất, đủ cho chatbot tư vấn

# CORS: đọc từ .env, mặc định chỉ localhost dev
_origins_raw = os.getenv("ALLOWED_ORIGINS", "http://localhost:5500,http://127.0.0.1:5500,http://localhost:8000")
ALLOWED_ORIGINS = [o.strip() for o in _origins_raw.split(",") if o.strip()]

SYSTEM_PROMPT = """Bạn là trợ lý tư vấn AI của Công ty TNHH Công nghệ Bản đồ GIS Quy Hoạch.
Tên bạn là "Gissy" — một chuyên gia GIS thân thiện, am hiểu sâu về Thông tư 16 và quy hoạch Việt Nam.

THÔNG TIN CÔNG TY:
- Tên: Công ty TNHH Công nghệ Bản đồ GIS Quy Hoạch
- Hotline/Zalo: 0332 945 089
- Dịch vụ chính: Lập hồ sơ quy hoạch trên GIS, chuyển đổi CAD → GIS chuẩn Thông tư 16
- Tiêu chuẩn: EPSG:5897, VN2000, GeoPackage, TT16/BXD, TT01/2021
- Thời gian: Hoàn thành 1-3 ngày làm việc
- Chính sách: Làm trước, thanh toán sau khi nghiệm thu
- Cam kết: Quét lỗi tự động, WebGIS viewer, hỗ trợ thẩm định trọn gói

DỊCH VỤ CHI TIẾT:
1. Chuyển đổi CAD (.dwg/.dxf) → GeoPackage chuẩn TT16
2. Quét lỗi topology tự động
3. Chuẩn hóa hệ tọa độ VN2000/EPSG:5897 và múi chiếu 3°
4. Đóng gói hồ sơ đúng cấu trúc Phụ lục II TT16
5. WebGIS viewer để thẩm định trực tuyến
6. Hỗ trợ hồ sơ năng lực, hồ sơ dự thầu, hồ sơ nghiệm thu
7. Đồng hành từ lần gặp chủ đầu tư đến nghiệm thu

GIÁ: Báo giá sau khi xem hồ sơ. Cạnh tranh, minh bạch. Làm trước trả sau.

QUY TẮC TRẢ LỜI:
- Trả lời bằng tiếng Việt, thân thiện, chuyên nghiệp
- Ngắn gọn, đúng trọng tâm (tối đa 3-4 câu mỗi lần, trừ khi cần giải thích kỹ)
- Luôn hướng khách hàng liên hệ Zalo 0332 945 089 khi cần tư vấn chi tiết hoặc báo giá
- KHÔNG bịa số liệu không có trong thông tin trên
- Khi khách hỏi giá cụ thể → nói "cần xem hồ sơ để báo giá chính xác, liên hệ Zalo 0332 945 089"
- Khi được hỏi về vấn đề ngoài phạm vi GIS/quy hoạch → lịch sự từ chối và hướng về dịch vụ GIS Quy Hoạch
- Mở đầu cuộc trò chuyện: giới thiệu bản thân là Gissy, hỏi khách cần hỗ trợ gì"""

# ── Rate Limiter ───────────────────────────────────────────────────
limiter = Limiter(key_func=get_remote_address, default_limits=["100/hour"])

# ── FastAPI app ────────────────────────────────────────────────────
app = FastAPI(title="GIS Quy Hoạch Chat API", docs_url=None, redoc_url=None)  # Tắt Swagger docs production

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,      # ✅ Chỉ cho phép domain cụ thể
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],     # ✅ Chỉ cho phép header cần thiết
)

# ── Pydantic Models với validation ────────────────────────────────
class Message(BaseModel):
    role: str
    content: str = Field(..., min_length=1, max_length=2000)   # ✅ Giới hạn độ dài

    @validator("role")
    def validate_role(cls, v):
        if v not in ("user", "assistant"):
            raise ValueError("role phải là 'user' hoặc 'assistant'")
        return v

class ChatRequest(BaseModel):
    messages: List[Message] = Field(..., min_items=1, max_items=20)  # ✅ Giới hạn số tin

class ChatResponse(BaseModel):
    reply: str
    error: str = ""

class ContactRequest(BaseModel):
    name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=20)
    email: str = Field("", max_length=100)
    project_type: str = Field("", max_length=100)
    message: str = Field("", max_length=2000)

class ContactResponse(BaseModel):
    status: str
    msg: str = ""
    error: str = ""

# ── Endpoints ─────────────────────────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
@limiter.limit("15/minute")             # ✅ Rate limit: 15 tin/phút mỗi IP
async def chat(request: Request, req: ChatRequest):
    if not CLAUDE_API_KEY:
        return ChatResponse(
            reply="",
            error="Chưa cấu hình API key. Vui lòng thêm ANTHROPIC_API_KEY vào file .env"
        )
    try:
        client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        msgs = [{"role": m.role, "content": m.content} for m in req.messages]
        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=msgs,
        )
        return ChatResponse(reply=response.content[0].text)
    except anthropic.AuthenticationError:
        return ChatResponse(reply="", error="API key không hợp lệ")
    except Exception as e:
        return ChatResponse(reply="", error=str(e))

@app.post("/contact", response_model=ContactResponse)
@limiter.limit("5/minute")
async def submit_contact(request: Request, req: ContactRequest):
    try:
        file_exists = os.path.isfile("contacts.csv")
        with open("contacts.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Time", "Name", "Phone", "Email", "Project Type", "Message"])
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), req.name, req.phone, req.email, req.project_type, req.message])
        return ContactResponse(status="ok", msg="Đã lưu liên hệ")
    except Exception as e:
        return ContactResponse(status="error", error=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL}

if __name__ == "__main__":
    import uvicorn
    if not CLAUDE_API_KEY:
        print("⚠️  CẢNH BÁO: ANTHROPIC_API_KEY chưa được đặt trong .env — chat sẽ không hoạt động!")
    print(f"🔐 CORS cho phép: {ALLOWED_ORIGINS}")
    print("🤖 GIS Quy Hoạch AI Chat đang chạy tại http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)  # ✅ Bind localhost, không phải 0.0.0.0
