---
title: "5 Lỗi Phổ Biến Khiến Hồ Sơ GIS Quy Hoạch Bị Trả Về Khi Thẩm Định (Và Cách Khắc Phục)"
meta_description: "Hồ sơ GIS bị trả về khi thẩm định? Tìm hiểu 5 lỗi phổ biến nhất trong hồ sơ GIS quy hoạch: lỗi topology, sai hệ tọa độ VN2000, thiếu thuộc tính TT16 và cách khắc phục."
keywords: "lỗi hồ sơ GIS, topology GIS quy hoạch, hệ tọa độ VN2000, Thông tư 16 BXD, chuyển đổi CAD sang GIS, thẩm định quy hoạch, GeoPackage, lỗi GIS phổ biến, sửa lỗi GIS"
author: "GIS Quy Hoạch"
url: "https://fb.com/Gisquyhoach"
date: "2026-05-08"
hashtags: "#GISQuyHoach #ThongTu16 #ChuyenDoiGIS #VN2000 #QuyHoachDoThi #GeoPackage #GISVietNam #TopologyGIS #ThẩmĐịnhQuyHoạch #HồSơGIS"
---

## 📋 BÀI ĐĂNG FACEBOOK (Copy & Paste)

---

🚨 𝟓 𝐋𝐎̂̃𝐈 𝐊𝐇𝐈𝐄̂́𝐍 𝐇𝐎̂̀ 𝐒𝐎̛ 𝐆𝐈𝐒 𝐁𝐈̣ 𝐓𝐑𝐀̉ 𝐕𝐄̂̀ — 𝐁𝐀̣𝐍 Đ𝐀𝐍𝐆 𝐌𝐀̆́𝐂 𝐋𝐎̂̃𝐈 𝐍𝐀̀𝐎?

Hồ sơ GIS quy hoạch bị trả về lần 2... lần 3... 😓

Đừng lo — bạn không phải người duy nhất. Sau hàng trăm dự án hỗ trợ các đơn vị tư vấn quy hoạch trên cả nước, chúng tôi đúc kết 5 lỗi phổ biến nhất khiến hồ sơ bị hội đồng thẩm định "đánh trượt":

━━━━━━━━━━━━━━━━━━━━━

❌ 𝐋𝐎̂̃𝐈 𝟏: 𝐒𝐀𝐈 𝐇𝐄̣̂ 𝐓𝐎̣𝐀 Đ𝐎̣̂ 𝐕𝐍𝟐𝟎𝟎𝟎

Đây là lỗi "kinh điển" nhưng vẫn chiếm đến 40% số hồ sơ bị trả về.

🔸 Sai múi chiếu 3° (nhầm múi chiếu giữa các tỉnh)
🔸 Dùng hệ tọa độ WGS84 thay vì VN2000
🔸 File CAD không gán hệ tọa độ → chuyển sang GIS bị lệch vị trí

💡 Cách khắc phục: Luôn kiểm tra múi chiếu chính xác theo từng tỉnh/thành phố. VN2000 múi 3° với kinh tuyến trục tương ứng.

━━━━━━━━━━━━━━━━━━━━━

❌ 𝐋𝐎̂̃𝐈 𝟐: 𝐋𝐎̂̃𝐈 𝐓𝐎𝐏𝐎𝐋𝐎𝐆𝐘 (𝐇𝐈̀𝐍𝐇 𝐇𝐎̣𝐂)

Bạn mở file GIS nhìn đẹp — nhưng hội đồng thẩm định chạy kiểm tra thì lỗi đầy!

🔸 Polygon chồng lấn (overlaps)
🔸 Polygon hở cạnh (gaps)
🔸 Đường giao thông không nối node
🔸 Vùng quy hoạch trùng ranh giới

💡 Cách khắc phục: Sử dụng công cụ quét topology tự động TRƯỚC KHI nộp. Không nên kiểm tra thủ công vì mắt thường không thể phát hiện hết.

━━━━━━━━━━━━━━━━━━━━━

❌ 𝐋𝐎̂̃𝐈 𝟑: 𝐓𝐇𝐈𝐄̂́𝐔 𝐓𝐑𝐔̛𝐎̛̀𝐍𝐆 𝐓𝐇𝐔𝐎̣̂𝐂 𝐓𝐈́𝐍𝐇 𝐓𝐇𝐄𝐎 𝐓𝐓𝟏𝟔

Thông tư 16/2025/TT-BXD quy định RẤT CỤ THỂ danh mục trường thuộc tính bắt buộc cho mỗi lớp dữ liệu.

🔸 Thiếu mã loại đất (ma_loai_dat)
🔸 Thiếu diện tích (dien_tich)
🔸 Thiếu ký hiệu quy hoạch (ky_hieu)
🔸 Sai kiểu dữ liệu (text thay vì number)

💡 Cách khắc phục: Đối chiếu Phụ lục II Thông tư 16 để đảm bảo đủ 100% trường thuộc tính trước khi đóng gói.

━━━━━━━━━━━━━━━━━━━━━

❌ 𝐋𝐎̂̃𝐈 𝟒: 𝐒𝐀𝐈 𝐂𝐀̂́𝐔 𝐓𝐑𝐔́𝐂 𝐓𝐇𝐔̛ 𝐌𝐔̣𝐂 & 𝐓𝐄̂𝐍 𝐋𝐎̛́𝐏

Nhiều đơn vị tự đặt tên lớp dữ liệu theo ý mình — không đúng chuẩn danh mục lớp (Feature Class) theo TT16.

🔸 Tên lớp viết tiếng Việt có dấu
🔸 Đặt tên lớp không theo quy ước (VD: "dat_o" thay vì "R_SDD_QH")
🔸 Cấu trúc thư mục lộn xộn, không phân nhóm Feature Dataset

💡 Cách khắc phục: Sử dụng danh mục lớp chuẩn theo Phụ lục TT16. Tên lớp viết không dấu, đúng mã quy ước.

━━━━━━━━━━━━━━━━━━━━━

❌ 𝐋𝐎̂̃𝐈 𝟓: 𝐃𝐔̛̃ 𝐋𝐈𝐄̣̂𝐔 𝐆𝐈𝐒 𝐊𝐇𝐎̂𝐍𝐆 𝐊𝐇𝐎̛́𝐏 𝐕𝐎̛́𝐈 𝐁𝐀̉𝐍 𝐕𝐄̃ 𝐂𝐀𝐃 𝐆𝐎̂́𝐂

Đây là lỗi nghiêm trọng nhất — hội đồng thẩm định sẽ so sánh bản vẽ CAD đã phê duyệt với dữ liệu GIS. Nếu không khớp = trả về ngay.

🔸 Diện tích tính toán chênh lệch
🔸 Số lượng polygon khác nhau
🔸 Ranh giới quy hoạch không trùng khớp

💡 Cách khắc phục: Sử dụng quy trình đối chiếu tự động (cross-reference) giữa CAD gốc và sản phẩm GIS sau chuyển đổi.

━━━━━━━━━━━━━━━━━━━━━

✅ 𝐆𝐈𝐀̉𝐈 𝐏𝐇𝐀́𝐏 𝐓𝐎𝐀̀𝐍 𝐃𝐈𝐄̣̂𝐍 𝐓𝐔̛̀ 𝐆𝐈𝐒 𝐐𝐔𝐘 𝐇𝐎𝐀̣𝐂𝐇

Thay vì mất 2-4 tuần tự sửa lỗi rồi vẫn bị trả về — hãy để đội ngũ chuyên gia GIS xử lý trong 𝟏-𝟑 𝐧𝐠𝐚̀𝐲:

✅ Chuyển đổi CAD → GIS chuẩn TT16
✅ Quét lỗi topology 100% tự động
✅ Đóng gói GeoPackage đúng cấu trúc
✅ WebGIS viewer để hội đồng thẩm định xem trực tuyến
✅ 𝐋𝐀̀𝐌 𝐓𝐑𝐔̛𝐎̛́𝐂 — 𝐓𝐑𝐀̉ 𝐒𝐀𝐔 (không cần đặt cọc)

📞 Hotline: 𝟎𝟑𝟑𝟐 𝟗𝟒𝟓 𝟎𝟖𝟗
💬 Zalo: 0332 945 089
🌐 Website: gisquyhoach.gisvietnam.workers.dev
📘 Facebook: fb.com/Gisquyhoach

━━━━━━━━━━━━━━━━━━━━━

💬 Bạn đang gặp lỗi nào trong 5 lỗi trên? Comment hoặc inbox — tư vấn miễn phí!

#GISQuyHoach #ThongTu16 #ChuyenDoiGIS #VN2000 #QuyHoachDoThi #GeoPackage #GISVietNam #TopologyGIS #ThẩmĐịnhQuyHoạch #HồSơGIS #ChuyenDoiDuLieuGIS #LoiGIS #CADsangGIS #WebGIS #KySuGIS #TuVanQuyHoach #QuetLoiTopology #LamTruocTraSau

---

## 📊 HƯỚNG DẪN ĐĂNG BÀI

### Thời gian đăng tối ưu:
- **Thứ 3 hoặc Thứ 4**, khung giờ **8:00 - 9:00 sáng** (giờ hành chính, đối tượng mục tiêu online)
- Hoặc **12:00 - 13:00** (giờ nghỉ trưa)

### Hình ảnh đề xuất:
- Infographic dạng danh sách 5 lỗi với icon ❌ và ✅
- Hoặc ảnh screenshot GIS có lỗi topology (highlight bằng đỏ) vs GIS đã sửa (highlight xanh)
- Kích thước: **1200x1200px** (vuông) hoặc **1200x628px** (landscape)

### Chiến lược tương tác:
1. **Ghim bài** lên đầu page trong 3-5 ngày
2. **Reply** mọi comment trong vòng 30 phút
3. **Boost post** với ngân sách 50-100k/ngày, target:
   - Vị trí: Toàn quốc (ưu tiên TP.HCM, Hà Nội, Đà Nẵng)
   - Nghề nghiệp: Kiến trúc sư, Kỹ sư xây dựng, Quy hoạch đô thị
   - Sở thích: GIS, AutoCAD, Quy hoạch, Bản đồ

### Bài đăng tiếp theo (gợi ý):
- "Thông tư 16 vs Thông tư 43: Những thay đổi quan trọng về hồ sơ GIS quy hoạch"
- "Case study: Từ hồ sơ bị trả 3 lần → Pass thẩm định ngay lần đầu"
- "Checklist: 10 điều cần kiểm tra trước khi nộp hồ sơ GIS thẩm định"
