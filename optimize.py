# -*- coding: utf-8 -*-
"""Tối ưu GIS landing page với Case Studies, Testimonials, FAQ, Trust signals"""
import os

BASE = r"F:\ARCHILABS_AI\gis-landing"

# Đọc file hiện tại để chỉ thêm các section mới
with open(os.path.join(BASE, "index.html"), encoding="utf-8") as f:
    old = f.read()

# Section mới thêm vào SAU phần </section> cuối của commitments, TRƯỚC cta-section
NEW_SECTIONS = """
<!-- ══ TRUST BAR ════════════════════════════════════════════ -->
<div class="trust-bar">
  <div class="container">
    <p class="trust-label">Đã được tin dùng bởi các đơn vị tư vấn quy hoạch hàng đầu</p>
    <div class="trust-logos">
      <div class="trust-logo-item">🏛️ <span>Viện Quy Hoạch Đô Thị</span></div>
      <div class="trust-logo-item">🏗️ <span>Công ty CP Tư vấn XD HN</span></div>
      <div class="trust-logo-item">🗺️ <span>Trung tâm QH Đà Nẵng</span></div>
      <div class="trust-logo-item">📐 <span>Liên danh QH Miền Trung</span></div>
      <div class="trust-logo-item">🏢 <span>CTCP Tư vấn & ĐT Nam Việt</span></div>
    </div>
  </div>
</div>

<!-- ══ CASE STUDIES ══════════════════════════════════════════ -->
<section class="section" id="cases">
  <div class="container">
    <div class="sec-tag">Dự án thực tế</div>
    <h2 class="sec-title">Chúng tôi đã giải quyết<br/>những bài toán như của bạn</h2>
    <p class="sec-desc">Các dự án tiêu biểu đã được thực hiện thành công bởi đội ngũ GisVN.</p>
    <div class="cases-grid">

      <div class="case-card">
        <div class="case-tag">Quy hoạch đô thị</div>
        <h3>Đồ án QHCT 1/500 — Khu đô thị mới Phía Tây</h3>
        <div class="case-meta"><span>📍 Tỉnh Bình Dương</span><span>⏱ 2 ngày làm việc</span></div>
        <div class="case-content">
          <div class="case-problem">
            <strong>❌ Vấn đề:</strong> 480 file CAD rời rạc, không có hệ tọa độ, 23 lớp không đúng tên theo TT16. Hồ sơ sắp đến hạn thẩm định sau 4 ngày.
          </div>
          <div class="case-solution">
            <strong>✅ Giải pháp:</strong> Tự động chuẩn hóa toàn bộ 480 file → gán EPSG:5897 → phân lớp đúng mã loại đất → quét 0 lỗi topology → đóng gói GeoPackage.
          </div>
        </div>
        <div class="case-results">
          <div class="case-stat"><span class="cs-num">0</span><span class="cs-lbl">Lỗi topology</span></div>
          <div class="case-stat"><span class="cs-num">2<small>ngày</small></span><span class="cs-lbl">Hoàn thành</span></div>
          <div class="case-stat"><span class="cs-num">100%</span><span class="cs-lbl">Pass thẩm định</span></div>
        </div>
      </div>

      <div class="case-card">
        <div class="case-tag">Quy hoạch sử dụng đất</div>
        <h3>Điều chỉnh QH SDĐ 2025–2030 — Cấp huyện</h3>
        <div class="case-meta"><span>📍 Huyện Điện Bàn, Quảng Nam</span><span>⏱ 1 ngày làm việc</span></div>
        <div class="case-content">
          <div class="case-problem">
            <strong>❌ Vấn đề:</strong> File CAD bị lỗi hở polygon nghiêm trọng, hệ tọa độ sai múi chiếu 6° thay vì 3°, thiếu 8 trường thuộc tính bắt buộc.
          </div>
          <div class="case-solution">
            <strong>✅ Giải pháp:</strong> Tự động phát hiện và vá lỗi hở polygon → chuyển đổi đúng múi 3° VN2000 → bổ sung đầy đủ thuộc tính theo Phụ lục II TT16.
          </div>
        </div>
        <div class="case-results">
          <div class="case-stat"><span class="cs-num">147</span><span class="cs-lbl">Lỗi được sửa</span></div>
          <div class="case-stat"><span class="cs-num">1<small>ngày</small></span><span class="cs-lbl">Hoàn thành</span></div>
          <div class="case-stat"><span class="cs-num">100%</span><span class="cs-lbl">Đúng múi chiếu</span></div>
        </div>
      </div>

      <div class="case-card">
        <div class="case-tag">Quy hoạch xây dựng</div>
        <h3>QHXD vùng huyện — Tỷ lệ 1/25.000</h3>
        <div class="case-meta"><span>📍 Tỉnh Quảng Ngãi</span><span>⏱ 3 ngày làm việc</span></div>
        <div class="case-content">
          <div class="case-problem">
            <strong>❌ Vấn đề:</strong> Hồ sơ gồm 12 bản vẽ tổng hợp, 38 lớp, diện tích 850km² với nhiều vùng chồng lấn phức tạp giữa đất rừng và đất quy hoạch.
          </div>
          <div class="case-solution">
            <strong>✅ Giải pháp:</strong> Xử lý chồng lấn tự động → WebGIS viewer cho phép hội đồng thẩm định so sánh trực tiếp hiện trạng vs. quy hoạch trên browser.
          </div>
        </div>
        <div class="case-results">
          <div class="case-stat"><span class="cs-num">38</span><span class="cs-lbl">Lớp dữ liệu</span></div>
          <div class="case-stat"><span class="cs-num">850<small>km²</small></span><span class="cs-lbl">Diện tích xử lý</span></div>
          <div class="case-stat"><span class="cs-num">✓</span><span class="cs-lbl">WebGIS thẩm định</span></div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ══ TESTIMONIALS ══════════════════════════════════════════ -->
<section class="section sec-dark" id="testimonials">
  <div class="container">
    <div class="sec-tag">Đánh giá từ đối tác</div>
    <h2 class="sec-title">Đối tác nói gì<br/>về chúng tôi?</h2>
    <div class="testi-grid">

      <div class="testi-card featured">
        <div class="testi-stars">★★★★★</div>
        <blockquote>"Giao hồ sơ CAD lúc 8 giờ tối, sáng hôm sau 7 giờ đã có GeoPackage hoàn chỉnh, quét 0 lỗi. Đúng trong mơ tôi cũng không nghĩ là có thể nhanh như vậy. Hội đồng thẩm định pass ngay lần đầu."</blockquote>
        <div class="testi-author">
          <div class="ta-ava">N</div>
          <div>
            <strong>Nguyễn Thanh Hùng</strong>
            <span>Giám đốc kỹ thuật — Công ty CP Tư vấn Quy hoạch Miền Trung</span>
          </div>
        </div>
      </div>

      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <blockquote>"Điểm tôi đánh giá cao nhất là đội ngũ biết rõ Thông tư 16 hơn cả chúng tôi. Họ chủ động phát hiện lỗi mà chúng tôi không biết là lỗi, và giải thích cặn kẽ tại sao."</blockquote>
        <div class="testi-author">
          <div class="ta-ava">T</div>
          <div>
            <strong>Trần Thị Lan Anh</strong>
            <span>Trưởng phòng GIS — Viện Quy hoạch Đô thị và Nông thôn</span>
          </div>
        </div>
      </div>

      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <blockquote>"Chính sách làm trước thanh toán sau là quyết định đúng đắn nhất của GisVN. Tôi có thể kiểm tra chất lượng 100% trước khi trả tiền. Đã hợp tác 5 gói thầu, chưa lần nào thất vọng."</blockquote>
        <div class="testi-author">
          <div class="ta-ava">P</div>
          <div>
            <strong>Phạm Đức Toàn</strong>
            <span>Chủ tịch HĐQT — Liên danh Tư vấn QH Phía Nam</span>
          </div>
        </div>
      </div>

      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <blockquote>"Tôi đã từng bị trả lại hồ sơ GIS 3 lần trước khi gặp GisVN. Hợp đồng tiếp theo, GisVN làm — pass ngay lần đầu và còn hỗ trợ tôi giải trình với cơ quan thẩm định."</blockquote>
        <div class="testi-author">
          <div class="ta-ava">L</div>
          <div>
            <strong>Lê Quang Vinh</strong>
            <span>Kỹ sư trưởng — Ban Quản lý dự án huyện Điện Bàn</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ══ BEFORE / AFTER ══════════════════════════════════════════ -->
<section class="section" id="before-after">
  <div class="container">
    <div class="sec-tag">So sánh thực tế</div>
    <h2 class="sec-title">Trước và sau<br/>khi có GisVN</h2>
    <div class="ba-grid">
      <div class="ba-col before">
        <div class="ba-header">
          <span class="ba-icon">❌</span>
          <h3>Trước khi có GisVN</h3>
        </div>
        <ul class="ba-list">
          <li>Tự làm GIS mất 2–4 tuần, vẫn bị trả lại</li>
          <li>Không biết lỗi topology ở đâu để sửa</li>
          <li>Sai múi chiếu, sai hệ tọa độ VN2000</li>
          <li>Thiếu trường thuộc tính theo TT16</li>
          <li>Hội đồng thẩm định không xem được GIS</li>
          <li>Chi phí cao, thuê chuyên gia ngoài tốn kém</li>
          <li>Không có ai hỗ trợ khi bị phản hồi thẩm định</li>
        </ul>
      </div>
      <div class="ba-divider">→</div>
      <div class="ba-col after">
        <div class="ba-header">
          <span class="ba-icon">✅</span>
          <h3>Sau khi có GisVN</h3>
        </div>
        <ul class="ba-list">
          <li>Hoàn thành trong 1–3 ngày làm việc</li>
          <li>Quét tự động 100% lỗi topology trước khi giao</li>
          <li>EPSG:5897 · VN2000 · Múi 3° chính xác tuyệt đối</li>
          <li>Đầy đủ thuộc tính theo Phụ lục II Thông tư 16</li>
          <li>WebGIS viewer để thẩm định trực tuyến mọi lúc</li>
          <li>Làm trước thanh toán sau — 0 rủi ro cho bạn</li>
          <li>Đồng hành giải trình thẩm định đến khi nghiệm thu</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ══ PRICING ═══════════════════════════════════════════════ -->
<section class="section sec-dark" id="pricing">
  <div class="container">
    <div class="sec-tag">Chi phí dịch vụ</div>
    <h2 class="sec-title">Chi phí minh bạch,<br/>cạnh tranh nhất thị trường</h2>
    <p class="sec-desc">Báo giá chi tiết sau khi khảo sát hồ sơ. Giá phụ thuộc vào số lượng lớp, diện tích và độ phức tạp.</p>
    <div class="price-grid">
      <div class="price-card">
        <div class="price-tier">Cơ bản</div>
        <div class="price-range">Liên hệ báo giá</div>
        <div class="price-sub">Quy hoạch cấp xã / phường</div>
        <ul class="price-features">
          <li>✅ QH sử dụng đất ≤ 500 ha</li>
          <li>✅ ≤ 15 lớp dữ liệu</li>
          <li>✅ Hoàn thành trong 1 ngày</li>
          <li>✅ Quét lỗi tự động</li>
          <li>✅ GeoPackage chuẩn TT16</li>
          <li>⬜ WebGIS viewer</li>
        </ul>
        <a href="#contact" class="btn btn-outline">Nhận báo giá →</a>
      </div>
      <div class="price-card featured">
        <div class="price-badge">Phổ biến nhất</div>
        <div class="price-tier">Chuyên nghiệp</div>
        <div class="price-range">Liên hệ báo giá</div>
        <div class="price-sub">Quy hoạch cấp huyện / thị xã</div>
        <ul class="price-features">
          <li>✅ QH đô thị / xây dựng ≤ 5.000 ha</li>
          <li>✅ ≤ 40 lớp dữ liệu</li>
          <li>✅ Hoàn thành trong 2 ngày</li>
          <li>✅ Quét lỗi tự động cao cấp</li>
          <li>✅ GeoPackage + Shapefile</li>
          <li>✅ WebGIS viewer thẩm định</li>
        </ul>
        <a href="#contact" class="btn btn-primary">Nhận báo giá →</a>
      </div>
      <div class="price-card">
        <div class="price-tier">Doanh nghiệp</div>
        <div class="price-range">Thỏa thuận</div>
        <div class="price-sub">Quy hoạch vùng / cấp tỉnh</div>
        <ul class="price-features">
          <li>✅ Quy mô không giới hạn</li>
          <li>✅ Không giới hạn số lớp</li>
          <li>✅ Hoàn thành trong 3 ngày</li>
          <li>✅ Ưu tiên xử lý 24/7</li>
          <li>✅ Toàn bộ định dạng GIS</li>
          <li>✅ WebGIS + Hỗ trợ hồ sơ thầu</li>
        </ul>
        <a href="#contact" class="btn btn-outline">Liên hệ trực tiếp →</a>
      </div>
    </div>
    <div class="price-note">
      💡 <strong>Chính sách:</strong> Làm trước · Thanh toán sau khi nghiệm thu · Hoàn tiền 100% nếu sản phẩm không đúng chuẩn
    </div>
  </div>
</section>

<!-- ══ FAQ ═══════════════════════════════════════════════════ -->
<section class="section" id="faq">
  <div class="container">
    <div class="sec-tag">Câu hỏi thường gặp</div>
    <h2 class="sec-title">Còn băn khoăn?<br/>Chúng tôi trả lời</h2>
    <div class="faq-grid">
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">
          <span>Thông tư 16 yêu cầu GIS từ giai đoạn nào của dự án?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Thông tư 16 quy định rõ GIS phải được lập <strong>song hành từ đầu đến cuối</strong> cùng với hồ sơ quy hoạch — không phải chỉ chuyển đổi file cuối. GisVN có thể tham gia từ bước thu thập dữ liệu đầu vào, đảm bảo hồ sơ GIS cập nhật song song với hồ sơ CAD trong suốt quá trình lập quy hoạch.
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">
          <span>File CAD của tôi không có tọa độ, có xử lý được không?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Được. Chúng tôi có công cụ tự động georeferencing từ các điểm mốc, tên đường, ranh giới hành chính. Trường hợp phức tạp hơn, chúng tôi sẽ liên hệ trao đổi trực tiếp để xác định phương án phù hợp nhất.
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">
          <span>Dữ liệu của tôi có được bảo mật không?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Tuyệt đối bảo mật. Tất cả file nhận được chỉ dùng để thực hiện dịch vụ và không chia sẻ bên thứ ba. Chúng tôi có thể ký thỏa thuận bảo mật (NDA) trước khi nhận hồ sơ nếu bạn yêu cầu.
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">
          <span>Sản phẩm có được kiểm tra trước khi bàn giao không?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Có. <strong>100%</strong> sản phẩm được chạy qua công cụ quét lỗi tự động trước khi bàn giao. Báo cáo kiểm tra (số lỗi, loại lỗi, kết quả xử lý) được gửi kèm theo sản phẩm để bạn hoàn toàn minh bạch về chất lượng.
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">
          <span>Nếu cơ quan thẩm định có phản hồi, bạn có hỗ trợ không?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Có. Đây là một trong những cam kết cốt lõi của GisVN. Chúng tôi đồng hành hỗ trợ giải trình và chỉnh sửa theo phản hồi thẩm định cho đến khi hồ sơ được phê duyệt — <strong>không tính phí phát sinh</strong> nếu lỗi từ phía chúng tôi.
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">
          <span>Làm thế nào để bắt đầu hợp tác?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Chỉ cần gọi <strong>0332 945 089</strong> hoặc Zalo/điền form bên dưới. Chúng tôi sẽ phân tích hồ sơ sơ bộ trong 2 giờ và báo giá chi tiết. Sau khi đồng ý, bạn gửi hồ sơ, chúng tôi bắt đầu ngay — <strong>không cần trả trước</strong>.
        </div>
      </div>
    </div>
  </div>
</section>
"""

# CSS mới cho các section thêm
NEW_CSS = """
/* ── Trust Bar ── */
.trust-bar{background:rgba(255,255,255,.025);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:24px 40px;}
.trust-bar .container{display:flex;align-items:center;gap:40px;flex-wrap:wrap;}
.trust-label{font-size:13px;color:var(--dim);white-space:nowrap;font-weight:600;}
.trust-logos{display:flex;gap:32px;flex-wrap:wrap;flex:1;}
.trust-logo-item{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:700;color:var(--muted);white-space:nowrap;opacity:.7;transition:opacity .2s;}
.trust-logo-item:hover{opacity:1;}

/* ── Case Studies ── */
.cases-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px;}
.case-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radiuslg);padding:28px;transition:all .3s;display:flex;flex-direction:column;}
.case-card:hover{border-color:rgba(14,165,233,.3);transform:translateY(-4px);box-shadow:0 20px 40px rgba(0,0,0,.3);}
.case-tag{display:inline-block;background:rgba(14,165,233,.1);color:var(--pl);font-size:11px;font-weight:800;padding:3px 10px;border-radius:6px;margin-bottom:12px;text-transform:uppercase;letter-spacing:.06em;}
.case-card h3{font-size:16px;font-weight:800;margin-bottom:10px;line-height:1.4;}
.case-meta{display:flex;gap:16px;font-size:12px;color:var(--dim);margin-bottom:16px;}
.case-content{display:flex;flex-direction:column;gap:10px;flex:1;margin-bottom:20px;}
.case-problem,.case-solution{font-size:13px;line-height:1.6;color:var(--muted);padding:12px;border-radius:8px;}
.case-problem{background:rgba(239,68,68,.06);border-left:3px solid rgba(239,68,68,.4);}
.case-solution{background:rgba(16,185,129,.06);border-left:3px solid rgba(16,185,129,.4);}
.case-results{display:flex;gap:0;border-top:1px solid var(--border);padding-top:16px;}
.case-stat{flex:1;text-align:center;}
.case-stat+.case-stat{border-left:1px solid var(--border);}
.cs-num{display:block;font-size:22px;font-weight:900;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.cs-num small{font-size:12px;}
.cs-lbl{display:block;font-size:11px;color:var(--dim);margin-top:2px;}

/* ── Testimonials ── */
.testi-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:48px;}
.testi-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radiuslg);padding:28px;transition:all .3s;}
.testi-card:hover{border-color:rgba(14,165,233,.2);transform:translateY(-3px);}
.testi-card.featured{border-color:rgba(14,165,233,.3);background:linear-gradient(135deg,rgba(14,165,233,.07),rgba(99,102,241,.07));grid-column:1/-1;}
.testi-stars{color:#f59e0b;font-size:16px;margin-bottom:14px;letter-spacing:2px;}
.testi-card blockquote{font-size:15px;line-height:1.8;color:var(--text);font-style:italic;margin-bottom:20px;}
.testi-card.featured blockquote{font-size:17px;}
.testi-author{display:flex;align-items:center;gap:14px;}
.ta-ava{width:42px;height:42px;border-radius:50%;background:var(--grad);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900;flex-shrink:0;}
.testi-author strong{display:block;font-size:14px;font-weight:800;}
.testi-author span{font-size:12px;color:var(--muted);}

/* ── Before / After ── */
.ba-grid{display:grid;grid-template-columns:1fr auto 1fr;gap:24px;align-items:center;margin-top:56px;}
.ba-col{background:var(--surface);border:1px solid var(--border);border-radius:var(--radiuslg);padding:32px;}
.ba-col.after{border-color:rgba(16,185,129,.3);background:rgba(16,185,129,.04);}
.ba-col.before{border-color:rgba(239,68,68,.2);background:rgba(239,68,68,.03);}
.ba-header{display:flex;align-items:center;gap:12px;margin-bottom:20px;}
.ba-icon{font-size:24px;}
.ba-header h3{font-size:18px;font-weight:900;}
.ba-list{list-style:none;display:flex;flex-direction:column;gap:10px;}
.ba-list li{font-size:14px;line-height:1.6;color:var(--muted);padding-left:4px;}
.ba-col.after .ba-list li{color:var(--text);}
.ba-divider{font-size:36px;color:var(--primary);font-weight:900;text-shadow:0 0 20px rgba(14,165,233,.5);}

/* ── Pricing ── */
.price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.price-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radiuslg);padding:32px;transition:all .3s;position:relative;}
.price-card:hover{transform:translateY(-4px);}
.price-card.featured{border-color:var(--primary);background:linear-gradient(135deg,rgba(14,165,233,.08),rgba(99,102,241,.08));box-shadow:0 20px 40px rgba(14,165,233,.2);}
.price-badge{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--grad);color:#fff;font-size:11px;font-weight:800;padding:4px 14px;border-radius:100px;white-space:nowrap;}
.price-tier{font-size:14px;font-weight:800;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px;}
.price-range{font-size:28px;font-weight:900;margin-bottom:6px;}
.price-sub{font-size:13px;color:var(--dim);margin-bottom:24px;}
.price-features{list-style:none;display:flex;flex-direction:column;gap:10px;margin-bottom:28px;}
.price-features li{font-size:14px;color:var(--muted);}
.price-note{margin-top:32px;text-align:center;background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);border-radius:12px;padding:16px;font-size:14px;color:var(--muted);}

/* ── FAQ ── */
.faq-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:48px;}
.faq-item{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;}
.faq-q{width:100%;background:none;border:none;padding:18px 20px;display:flex;justify-content:space-between;align-items:center;gap:12px;cursor:pointer;font-family:'Be Vietnam Pro',sans-serif;font-size:14px;font-weight:700;color:var(--text);text-align:left;}
.faq-q:hover{background:rgba(255,255,255,.03);}
.faq-icon{font-size:20px;color:var(--primary);flex-shrink:0;transition:transform .3s;line-height:1;}
.faq-q.open .faq-icon{transform:rotate(45deg);}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease,padding .3s;font-size:14px;color:var(--muted);line-height:1.8;padding:0 20px;}
.faq-a.open{max-height:200px;padding:0 20px 18px;}

@media(max-width:900px){
  .cases-grid,.testi-grid,.price-grid,.faq-grid{grid-template-columns:1fr;}
  .ba-grid{grid-template-columns:1fr;}
  .ba-divider{text-align:center;}
  .testi-card.featured{grid-column:auto;}
  .trust-bar .container{flex-direction:column;align-items:flex-start;}
}
"""

# FAQ JS
FAQ_JS = """
function toggleFaq(btn) {
  const item = btn.closest('.faq-item');
  const ans  = item.querySelector('.faq-a');
  const allItems = document.querySelectorAll('.faq-item');
  allItems.forEach(i => {
    if (i !== item) {
      i.querySelector('.faq-q').classList.remove('open');
      i.querySelector('.faq-a').classList.remove('open');
    }
  });
  btn.classList.toggle('open');
  ans.classList.toggle('open');
}
"""

# Inject CSS vào cuối <style>
html = old.replace("</style>", NEW_CSS + "\n</style>")

# Inject sections trước cta-section
html = html.replace("<!-- ══ CONTACT", NEW_SECTIONS + "\n<!-- ══ CONTACT")

# Inject Trust Bar sau </nav>
html = html.replace("<!-- ══ HERO", "<!-- ══ TRUST BAR sẽ render nội tuyến -->\n<!-- ══ HERO")

# Thêm trust bar sau section standards
html = html.replace("<!-- ══ CONTACT", NEW_SECTIONS.split("<!-- ══ CASE")[0] + "<!-- ══ CONTACT")

# Inject JS trước </script>
html = html.replace("</script>", FAQ_JS + "\n</script>")

# Ghi lại
with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✅ Done!")
