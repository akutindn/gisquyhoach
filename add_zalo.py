# -*- coding: utf-8 -*-
"""Tích hợp Zalo vào toàn bộ landing page GisVN"""
import os, re

BASE  = r"F:\ARCHILABS_AI\gis-landing"
PHONE = "0332945089"
ZALO  = f"https://zalo.me/{PHONE}"

with open(os.path.join(BASE,"index.html"), encoding="utf-8") as f:
    html = f.read()

# ── 1. Thay toàn bộ href="#contact" → Zalo, giữ nguyên nội dung btn ──
# Chỉ các btn có chứa chữ "tư vấn", "báo giá", "liên hệ", "ngay"
def zalo_href(m):
    btn = m.group(0)
    # Giữ nguyên các anchor nội trang như #features, #process, ...
    text_lower = btn.lower()
    if any(k in text_lower for k in ['tư vấn','báo giá','liên hệ ngay','bắt đầu ngay','nhận báo giá','liên hệ trực tiếp']):
        return btn.replace('href="#contact"', f'href="{ZALO}" target="_blank" rel="noopener"')
    return btn

html = re.sub(r'<a [^>]*href="#contact"[^>]*>.*?</a>', zalo_href, html, flags=re.DOTALL)

# ── 2. Thay anchor href="tel:..." → Zalo cũng ──
html = html.replace(
    f'href="tel:{PHONE}"',
    f'href="{ZALO}" target="_blank" rel="noopener"'
)

# ── 3. Nút "Liên hệ ngay" trong navbar → Zalo ──
html = html.replace(
    'href="#contact" class="btn btn-primary nav-cta"',
    f'href="{ZALO}" target="_blank" rel="noopener" class="btn btn-primary nav-cta"'
)

# ── 4. CSS Floating Zalo button + mobile sticky bar ──────────────────
ZALO_CSS = """
/* ── Floating Zalo button ── */
.zalo-float{position:fixed;bottom:28px;right:28px;z-index:9999;display:flex;flex-direction:column;align-items:flex-end;gap:8px;}
.zalo-fab{width:62px;height:62px;border-radius:50%;background:#0068ff;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(0,104,255,.5);cursor:pointer;text-decoration:none;position:relative;animation:zalo-pulse 2.5s infinite;}
@keyframes zalo-pulse{0%,100%{box-shadow:0 8px 24px rgba(0,104,255,.5),0 0 0 0 rgba(0,104,255,.4);}60%{box-shadow:0 8px 24px rgba(0,104,255,.5),0 0 0 14px rgba(0,104,255,0);}}
.zalo-fab svg{width:34px;height:34px;}
.zalo-tooltip{background:rgba(0,0,0,.85);color:#fff;font-size:13px;font-weight:700;padding:7px 14px;border-radius:8px;white-space:nowrap;backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.1);animation:tooltip-bounce .6s ease infinite alternate;}
@keyframes tooltip-bounce{from{transform:translateX(0);}to{transform:translateX(-4px);}}
.zalo-badge{position:absolute;top:-4px;right:-4px;background:#ef4444;color:#fff;font-size:10px;font-weight:900;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:2px solid var(--bg);}

/* ── Mobile sticky CTA bar ── */
.mobile-cta{display:none;position:fixed;bottom:0;left:0;right:0;z-index:998;background:rgba(5,11,24,.97);backdrop-filter:blur(16px);border-top:1px solid var(--border);padding:12px 16px;gap:10px;}
@media(max-width:768px){
  .mobile-cta{display:flex;}
  .zalo-float{bottom:80px;right:16px;}
  .zalo-fab{width:54px;height:54px;}
}
.mcta-call{flex:1;display:flex;align-items:center;justify-content:center;gap:8px;padding:13px;background:rgba(255,255,255,.06);border:1px solid var(--border);border-radius:12px;font-weight:800;font-size:14px;color:var(--text);text-decoration:none;}
.mcta-zalo{flex:1;display:flex;align-items:center;justify-content:center;gap:8px;padding:13px;background:#0068ff;border-radius:12px;font-weight:800;font-size:14px;color:#fff;text-decoration:none;box-shadow:0 4px 14px rgba(0,104,255,.4);}

/* ── Form cập nhật — nút Zalo trực tiếp ── */
.or-row{display:flex;align-items:center;gap:12px;grid-column:1/-1;margin:4px 0;}
.or-row::before,.or-row::after{content:'';flex:1;height:1px;background:var(--border);}
.or-row span{font-size:13px;color:var(--dim);white-space:nowrap;}
.btn-zalo-direct{grid-column:1/-1;display:flex;align-items:center;justify-content:center;gap:10px;padding:14px;background:#0068ff;border-radius:12px;font-family:'Be Vietnam Pro',sans-serif;font-weight:800;font-size:15px;color:#fff;border:none;cursor:pointer;text-decoration:none;box-shadow:0 8px 24px rgba(0,104,255,.35);transition:all .2s;}
.btn-zalo-direct:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(0,104,255,.5);}
"""

html = html.replace("</style>", ZALO_CSS + "\n</style>")

# ── 5. HTML Floating Zalo + Mobile sticky bar (trước </body>) ──────
ZALO_HTML = f"""
<!-- ══ FLOATING ZALO BUTTON ══════════════════════════════════ -->
<div class="zalo-float">
  <div class="zalo-tooltip">💬 Chat Zalo ngay!</div>
  <a class="zalo-fab" href="{ZALO}" target="_blank" rel="noopener" title="Chat Zalo tư vấn miễn phí">
    <span class="zalo-badge">1</span>
    <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="48" height="48" rx="24" fill="#0068FF"/>
      <path d="M10 24C10 16.268 16.268 10 24 10C31.732 10 38 16.268 38 24C38 31.732 31.732 38 24 38C21.4 38 19 37.3 16.9 36L11 38L12.8 32.4C11.1 30.1 10 27.2 10 24Z" fill="white"/>
      <path d="M17 22h3M22 22h2m3 0h2M17 26h14" stroke="#0068FF" stroke-width="2" stroke-linecap="round"/>
      <text x="16" y="27" font-family="Arial" font-size="10" font-weight="bold" fill="#0068FF">Zalo</text>
    </svg>
  </a>
</div>

<!-- ══ MOBILE STICKY CTA ══════════════════════════════════════ -->
<div class="mobile-cta">
  <a class="mcta-call" href="tel:{PHONE}">📞 Gọi ngay</a>
  <a class="mcta-zalo" href="{ZALO}" target="_blank" rel="noopener">
    <svg width="20" height="20" viewBox="0 0 48 48" fill="none"><path d="M10 24C10 16.268 16.268 10 24 10C31.732 10 38 16.268 38 24C38 31.732 31.732 38 24 38C21.4 38 19 37.3 16.9 36L11 38L12.8 32.4C11.1 30.1 10 27.2 10 24Z" fill="white"/></svg>
    Chat Zalo tư vấn
  </a>
</div>
"""

html = html.replace("</body>", ZALO_HTML + "\n</body>")

# ── 6. Thêm nút Zalo trực tiếp trong form contact ────────────────
ZALO_FORM_EXTRA = f"""
        <div class="or-row"><span>— hoặc tư vấn ngay qua —</span></div>
        <a class="btn-zalo-direct" href="{ZALO}" target="_blank" rel="noopener">
          <svg width="22" height="22" viewBox="0 0 48 48" fill="none"><path d="M10 24C10 16.268 16.268 10 24 10C31.732 10 38 16.268 38 24C38 31.732 31.732 38 24 38C21.4 38 19 37.3 16.9 36L11 38L12.8 32.4C11.1 30.1 10 27.2 10 24Z" fill="white"/></svg>
          💬 Nhắn tin Zalo — 0332 945 089
        </a>
"""

# Thêm sau nút submit
html = html.replace(
    "<p style=\"margin-top:12px;font-size:13px;color:var(--muted)\">Chúng tôi sẽ phản hồi trong vòng 30 phút trong giờ hành chính</p>",
    "<p style=\"margin-top:12px;font-size:13px;color:var(--muted)\">Chúng tôi sẽ phản hồi trong vòng 30 phút trong giờ hành chính</p>\n" + ZALO_FORM_EXTRA
)

# ── 7. Cập nhật cd-item phone → Zalo ────────────────────────────
html = html.replace(
    f'<a href="{ZALO}" target="_blank" rel="noopener" style="color:var(--pl)">{PHONE}</a>',
    f'<a href="{ZALO}" target="_blank" rel="noopener" style="color:#0068ff;font-weight:900">{PHONE} — Chat Zalo</a>'
)

with open(os.path.join(BASE,"index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Zalo integration hoàn tất!")
print(f"🔗 Zalo link: {ZALO}")
print("✓ Floating Zalo button (pulse animation)")
print("✓ Mobile sticky CTA bar (Gọi + Zalo)")
print("✓ Zalo direct button trong contact form")
print("✓ Tất cả CTA buttons → redirect Zalo")
