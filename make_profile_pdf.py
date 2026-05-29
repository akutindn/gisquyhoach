# -*- coding: utf-8 -*-
"""Generate GIS Quy Hoạch Capability Profile PDF"""
from fpdf import FPDF
import os

class ProfilePDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_auto_page_break(auto=True, margin=25)
        # Add Unicode font
        self.add_font('DVP', '', r'C:\Windows\Fonts\arial.ttf', uni=True)
        self.add_font('DVP', 'B', r'C:\Windows\Fonts\arialbd.ttf', uni=True)
        self.add_font('DVP', 'I', r'C:\Windows\Fonts\ariali.ttf', uni=True)
        self.BLUE = (30, 64, 175)
        self.SKY = (14, 165, 233)
        self.ORANGE = (249, 115, 22)
        self.DARK = (15, 23, 42)
        self.GRAY = (71, 85, 105)
        self.LIGHT = (241, 245, 249)

    def colored_cell(self, w, h, txt, color, font_size=10, bold=False, align='L', fill=False, fill_color=None):
        self.set_text_color(*color)
        self.set_font('DVP', 'B' if bold else '', font_size)
        if fill and fill_color:
            self.set_fill_color(*fill_color)
        self.cell(w, h, txt, ln=True, align=align, fill=fill)

    def section_tag(self, tag_text):
        self.ln(5)
        self.set_fill_color(239, 246, 255)
        self.set_text_color(*self.BLUE)
        self.set_font('DVP', 'B', 9)
        tw = self.get_string_width(tag_text) + 12
        x = self.get_x()
        self.cell(tw, 7, tag_text, ln=True, align='C', fill=True)
        self.ln(3)

    def section_title(self, title):
        self.set_text_color(*self.DARK)
        self.set_font('DVP', 'B', 18)
        self.multi_cell(0, 9, title)
        # Draw accent line
        self.set_fill_color(*self.SKY)
        self.cell(40, 2, '', fill=True, ln=True)
        self.ln(4)

    def body_text(self, txt):
        self.set_text_color(*self.GRAY)
        self.set_font('DVP', '', 10)
        self.multi_cell(0, 6, txt)
        self.ln(3)

    def draw_rounded_rect(self, x, y, w, h, r, fill_color):
        self.set_fill_color(*fill_color)
        self.rect(x, y, w, h, 'F')


def build_pdf():
    pdf = ProfilePDF()

    # ═══ COVER PAGE ═══
    pdf.add_page()
    # Blue gradient background
    pdf.set_fill_color(*pdf.BLUE)
    pdf.rect(0, 0, 210, 297, 'F')
    # Lighter overlay top
    pdf.set_fill_color(30, 80, 200)
    pdf.rect(0, 0, 210, 148, 'F')

    # Logo icon
    pdf.set_fill_color(255, 255, 255, )
    pdf.rect(85, 55, 40, 40, 'F')
    pdf.set_text_color(*pdf.BLUE)
    pdf.set_font('DVP', 'B', 28)
    pdf.set_xy(85, 62)
    pdf.cell(40, 20, 'GIS', align='C')

    # Title
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('DVP', 'B', 14)
    pdf.set_xy(0, 110)
    pdf.cell(210, 10, 'HỒ SƠ NĂNG LỰC', align='C', ln=True)

    pdf.set_font('DVP', 'B', 32)
    pdf.cell(210, 16, 'GIS Quy Hoạch', align='C', ln=True)

    # Orange line
    pdf.set_fill_color(*pdf.ORANGE)
    pdf.set_x(75)
    pdf.cell(60, 2, '', fill=True, ln=True)
    pdf.ln(8)

    pdf.set_font('DVP', '', 12)
    pdf.set_text_color(200, 220, 255)
    pdf.cell(210, 7, 'Chuyển đổi dữ liệu GIS • Thẩm định quy hoạch', align='C', ln=True)
    pdf.cell(210, 7, 'Tuân thủ Thông tư 16/2025 BXD', align='C', ln=True)

    # Contact info at bottom
    pdf.set_y(220)
    pdf.set_font('DVP', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    items = [
        ('Hotline:', '0332 945 089'),
        ('Zalo:', '0332 945 089'),
        ('Facebook:', 'fb.com/Gisquyhoach'),
        ('Website:', 'gisquyhoach.gisvietnam.workers.dev'),
    ]
    for label, val in items:
        pdf.set_x(55)
        pdf.set_font('DVP', '', 10)
        pdf.set_text_color(180, 200, 255)
        pdf.cell(30, 8, label, align='R')
        pdf.set_font('DVP', 'B', 10)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(80, 8, val, ln=True)

    pdf.set_y(270)
    pdf.set_font('DVP', 'I', 9)
    pdf.set_text_color(150, 180, 255)
    pdf.cell(210, 6, 'Năm 2025 • Phiên bản 1.0', align='C')

    # ═══ PAGE 2: GIỚI THIỆU ═══
    pdf.add_page()
    pdf.section_tag('GIỚI THIỆU')
    pdf.section_title('Chúng tôi là ai?')
    pdf.body_text(
        'GIS Quy Hoạch là đơn vị chuyên cung cấp dịch vụ chuyển đổi dữ liệu GIS '
        'và thẩm định quy hoạch hàng đầu Việt Nam. Với đội ngũ kỹ sư giàu kinh nghiệm '
        'từ các công ty GIS lâu đời, chúng tôi đã hỗ trợ hàng trăm đơn vị tư vấn quy hoạch '
        'trên cả nước hoàn thành hồ sơ GIS chuẩn Thông tư 16/2025 BXD.'
    )
    pdf.body_text(
        'Chúng tôi hiểu rằng việc lập quy hoạch trên GIS là một hạng mục song hành '
        'từ đầu đến cuối cùng với việc lập quy hoạch, chứ không đơn thuần là chuyển đổi '
        'file sản phẩm đã được phê duyệt từ CAD sang GIS. Vì vậy, chúng tôi cam kết đồng hành '
        'cùng đối tác từ buổi gặp đầu tiên đến khi nghiệm thu thành công.'
    )

    # Stats boxes
    pdf.ln(5)
    stats = [
        ('100%', 'Tuân thủ TT16'),
        ('1-3 ngày', 'Hoàn thành'),
        ('0đ', 'Trả trước'),
        ('50+', 'Dự án hoàn thành'),
    ]
    box_w = 40
    gap = 5
    start_x = (210 - (box_w * 4 + gap * 3)) / 2
    y = pdf.get_y() + 2
    for i, (num, lbl) in enumerate(stats):
        x = start_x + i * (box_w + gap)
        pdf.set_fill_color(*pdf.BLUE)
        pdf.rect(x, y, box_w, 28, 'F')
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('DVP', 'B', 16)
        pdf.set_xy(x, y + 4)
        pdf.cell(box_w, 8, num, align='C')
        pdf.set_font('DVP', '', 8)
        pdf.set_text_color(200, 215, 255)
        pdf.set_xy(x, y + 15)
        pdf.cell(box_w, 6, lbl, align='C')
    pdf.set_y(y + 38)

    # Tầm nhìn & Sứ mệnh
    pdf.ln(5)
    pdf.section_tag('TẦM NHÌN & SỨ MỆNH')
    pdf.section_title('Tầm nhìn')
    pdf.body_text(
        'Trở thành đối tác GIS tin cậy hàng đầu cho các đơn vị tư vấn quy hoạch tại Việt Nam, '
        'góp phần thúc đẩy chuyển đổi số trong lĩnh vực quy hoạch đô thị và nông thôn.'
    )
    pdf.section_title('Sứ mệnh')
    pdf.body_text(
        'Cung cấp giải pháp GIS toàn diện, chất lượng cao với chi phí hợp lý, '
        'giúp các đơn vị tư vấn quy hoạch dễ dàng đáp ứng yêu cầu Thông tư 16/2025 BXD '
        'mà không cần đầu tư xây dựng đội ngũ GIS nội bộ.'
    )

    # ═══ PAGE 3: DỊCH VỤ ═══
    pdf.add_page()
    pdf.section_tag('DỊCH VỤ')
    pdf.section_title('Giải pháp toàn diện cho hạng mục GIS')

    services = [
        ('🔄 Chuyển đổi CAD → GIS',
         'Chuyển đổi toàn bộ hồ sơ từ định dạng CAD (.dwg, .dxf) sang cơ sở dữ liệu GIS '
         'chuẩn GeoPackage theo đúng Thông tư 16. Hỗ trợ tất cả các loại đồ án quy hoạch: '
         'quy hoạch sử dụng đất, quy hoạch xây dựng, quy hoạch giao thông.'),
        ('🔬 Quét lỗi tự động',
         'Công cụ quét lỗi topology, sai hệ tọa độ, thiếu trường thuộc tính hoàn toàn tự động. '
         'Đảm bảo sản phẩm GIS đồng nhất 100% với hồ sơ CAD đầu vào.'),
        ('📦 Đóng gói hồ sơ chuẩn',
         'Cấu trúc thư mục, đặt tên lớp, trường thuộc tính đúng chuẩn theo quy định Thông tư 16. '
         'Thuận lợi tối đa cho việc thẩm định và nghiệm thu.'),
        ('🌐 Nền tảng WebGIS',
         'Hỗ trợ công cụ WebGIS để xem và tra cứu sản phẩm trực tiếp trên web. '
         'Thuận lợi cho hội đồng thẩm định xem cả bản CAD và GIS song song.'),
        ('📄 Hỗ trợ hồ sơ thầu',
         'Sẵn sàng đồng hành hỗ trợ năng lực, hồ sơ dự thầu, hồ sơ nghiệm thu '
         'liên quan đến hạng mục GIS.'),
        ('🤝 Đồng hành toàn gói thầu',
         'Từ buổi gặp đầu tiên với chủ đầu tư đến cái bắt tay sau nghiệm thu thành công — '
         'chúng tôi ở đây suốt hành trình cùng bạn.'),
    ]
    for title, desc in services:
        y = pdf.get_y()
        if y > 250:
            pdf.add_page()
        pdf.set_fill_color(*pdf.LIGHT)
        pdf.rect(pdf.l_margin, pdf.get_y(), 170, 1, 'F')
        pdf.ln(3)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_text_color(*pdf.GRAY)
        pdf.set_font('DVP', '', 10)
        pdf.multi_cell(170, 5.5, desc)
        pdf.ln(4)

    # ═══ PAGE 4: QUY TRÌNH ═══
    pdf.add_page()
    pdf.section_tag('QUY TRÌNH')
    pdf.section_title('Hoàn thành trong 1-3 ngày với 4 bước')

    steps = [
        ('BƯỚC 1', 'Tiếp nhận hồ sơ',
         'Bạn gửi hồ sơ CAD + tài liệu quy hoạch qua Zalo hoặc email. '
         'Chúng tôi phân tích và báo giá trong vòng 2 giờ.'),
        ('BƯỚC 2', 'Chuyển đổi & Xử lý',
         'Kỹ sư GIS triển khai chuyển đổi, phân lớp đúng mã loại đất, '
         'chuẩn hóa hệ tọa độ VN2000.'),
        ('BƯỚC 3', 'Quét lỗi & Kiểm tra',
         'Công cụ tự động quét toàn bộ lỗi topology, thuộc tính, '
         'đảm bảo khớp 100% với hồ sơ gốc.'),
        ('BƯỚC 4', 'Bàn giao & Hỗ trợ',
         'Giao GeoPackage + WebGIS viewer. Thanh toán sau khi nghiệm thu. '
         'Hỗ trợ thẩm định trọn gói.'),
    ]
    for step_num, title, desc in steps:
        y = pdf.get_y()
        # Step number badge
        pdf.set_fill_color(*pdf.SKY)
        pdf.rect(pdf.l_margin, y, 24, 8, 'F')
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('DVP', 'B', 8)
        pdf.set_xy(pdf.l_margin, y + 1)
        pdf.cell(24, 6, step_num, align='C')
        # Title
        pdf.set_xy(pdf.l_margin + 28, y)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 13)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_x(pdf.l_margin + 28)
        pdf.set_text_color(*pdf.GRAY)
        pdf.set_font('DVP', '', 10)
        pdf.multi_cell(140, 5.5, desc)
        pdf.ln(8)

    # ═══ CAM KẾT ═══
    pdf.ln(5)
    pdf.section_tag('CAM KẾT')
    pdf.section_title('Chúng tôi cam kết với bạn')

    commits = [
        ('Trách nhiệm cao • Uy tín • Tận tình',
         'Đồng hành cùng đối tác với tinh thần trách nhiệm cao nhất. '
         'Không bỏ lại đối tác giữa chừng dù gặp bất kỳ khó khăn nào.'),
        ('Bảo mật dữ liệu tuyệt đối',
         'Toàn bộ hồ sơ được xử lý trong môi trường kín. '
         'Ký hợp đồng bảo mật nếu cần.'),
        ('Tốc độ & Chất lượng',
         'Hoàn thành trong 1-3 ngày làm việc. '
         'Không để đối tác phải chờ quá deadline.'),
        ('Làm trước — Trả sau',
         'Không yêu cầu đặt cọc. '
         'Thanh toán sau khi kiểm tra và hài lòng với sản phẩm.'),
    ]
    for title, desc in commits:
        y = pdf.get_y()
        if y > 255:
            pdf.add_page()
        pdf.set_fill_color(240, 249, 255)
        h_box = 22
        pdf.rect(pdf.l_margin, y, 170, h_box, 'F')
        # Accent left bar
        pdf.set_fill_color(*pdf.SKY)
        pdf.rect(pdf.l_margin, y, 3, h_box, 'F')
        pdf.set_xy(pdf.l_margin + 6, y + 2)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 10)
        pdf.cell(0, 5, title, ln=True)
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_text_color(*pdf.GRAY)
        pdf.set_font('DVP', '', 9)
        pdf.multi_cell(160, 4.5, desc)
        pdf.set_y(y + h_box + 4)

    # ═══ DỰ ÁN KINH NGHIỆM THỰC TẾ ═══
    pdf.add_page()
    pdf.section_tag('KINH NGHIỆM THỰC TẾ')
    pdf.section_title('Dự án tiêu biểu trên toàn quốc')
    pdf.body_text(
        'Danh mục dự án tiêu biểu trải dài từ Bắc vào Nam, '
        'đa dạng quy mô và loại hình quy hoạch. 50+ dự án hoàn thành, '
        '30+ tỉnh/thành phố triển khai, 5.000+ km2 dữ liệu đã xử lý, '
        '100% hồ sơ pass thẩm định.'
    )

    projects = [
        ('MIỀN BẮC', 'QH vùng tỉnh',
         'QH vùng tỉnh Hòa Bình đến năm 2030 - Tỷ lệ 1/100.000',
         'Tỉnh Hòa Bình | 3 ngày làm việc',
         'Yêu cầu: Xây dựng CSDL GIS toàn tỉnh gồm 11 huyện, 210 xã, '
         'tích hợp dữ liệu quy hoạch sử dụng đất cấp tỉnh.',
         'Thực hiện: Chuẩn hóa 1.200+ polygon -> VN2000 múi 3 độ -> '
         'GeoPackage đa lớp -> WebGIS viewer phục vụ thẩm định HĐND tỉnh.',
         '210 đơn vị HC | 4.600 km2 | Pass thẩm định',
         (30, 64, 175)),  # Blue for North
        ('MIỀN BẮC', 'QH đô thị',
         'QHCT 1/500 Khu trung tâm HC - Đô thị mới Văn Giang',
         'Tỉnh Hưng Yên | 2 ngày làm việc',
         'Yêu cầu: Chuyển đổi toàn bộ hồ sơ QHCT tỷ lệ lớn, tích hợp dữ liệu '
         'hiện trạng và quy hoạch song song, khớp 100% bản vẽ CAD gốc.',
         'Thực hiện: Tự động chuẩn hóa 350 file DWG -> phân lớp ODT/CXD/GT/CX '
         'theo TT16 -> quét topology -> đóng gói chuẩn Phụ lục II.',
         '350 file DWG | 0 lỗi topology | 2 ngày hoàn thành',
         (30, 64, 175)),
        ('MIỀN TRUNG', 'QH xây dựng vùng',
         'QHXD vùng huyện 1/25.000 - Vùng Tây Nguyên mở rộng',
         'Tỉnh Đắk Lắk | 3 ngày làm việc',
         'Yêu cầu: Hồ sơ vùng huyện quy mô lớn, 15 huyện, dữ liệu đất lâm nghiệp '
         'phức tạp, nhiều vùng chồng lấn giữa đất rừng phòng hộ và đất quy hoạch.',
         'Thực hiện: Xử lý chồng lấn topology tự động -> tích hợp dữ liệu kiểm kê rừng '
         '-> WebGIS viewer để hội đồng so sánh hiện trạng và quy hoạch trực tuyến.',
         '15 huyện | 1.300 km2 | WebGIS thẩm định',
         (245, 158, 11)),  # Orange for Central
        ('MIỀN TRUNG', 'Điều chỉnh QH SDĐ',
         'Điều chỉnh QH SDĐ cấp huyện 2025-2030 - Ven biển miền Trung',
         'Huyện Thăng Bình, Quảng Nam | 1 ngày làm việc',
         'Yêu cầu: Điều chỉnh cục bộ hồ sơ GIS đã có, chuẩn hóa lại hệ tọa độ '
         'sau khi phát hiện sai múi chiếu, bổ sung 12 trường thuộc tính theo TT16.',
         'Thực hiện: Chuyển đổi toàn bộ sang múi 3 độ VN2000 -> tự động điền thuộc tính '
         'từ bảng tra mã loại đất -> kiểm tra đối chiếu với bản đồ giải thửa.',
         '12 trường bổ sung | 1 ngày | 100% đúng TT16',
         (245, 158, 11)),
        ('MIỀN NAM', 'QHCT đô thị',
         'QHCT 1/500 Khu đô thị - Thành phố mới Bình Dương',
         'Tỉnh Bình Dương | 2 ngày làm việc',
         'Yêu cầu: 480 file CAD rời rạc, không có hệ tọa độ, 23 lớp không đúng tên '
         'theo TT16. Hồ sơ cận hạn thẩm định — yêu cầu xử lý trong 48 giờ.',
         'Thực hiện: Chuẩn hóa tự động 480 file -> gán VN2000 múi 3 độ -> phân lớp '
         'đúng mã loại đất -> quét topology -> GeoPackage chuẩn Phụ lục II.',
         '480 file CAD | 0 lỗi topology | 100% pass thẩm định',
         (16, 185, 129)),  # Green for South
        ('MIỀN NAM', 'QH nông thôn',
         'Lập QH Chung XD xã NTM - Đồng bằng sông Cửu Long',
         'Tỉnh Đồng Tháp | 1 ngày làm việc',
         'Yêu cầu: Lập đồng thời hồ sơ GIS cho 12 xã nông thôn mới, tích hợp dữ liệu '
         'hạ tầng kỹ thuật (đường, kênh mương, điện), xuất GeoPackage nộp Sở XD.',
         'Thực hiện: Xây dựng template chuẩn 1 lần -> nhân rộng tự động cho 12 xã -> '
         'kiểm tra cross-reference giữa hồ sơ GIS và bản vẽ quy hoạch phê duyệt.',
         '12 xã NTM | 1 ngày | Nộp Sở XD thành công',
         (16, 185, 129)),
    ]

    for idx, (region, proj_type, title, meta, req, impl, results, color) in enumerate(projects):
        y = pdf.get_y()
        if y > 220:
            pdf.add_page()

        # Region + type badges
        pdf.set_fill_color(*color)
        pdf.rect(pdf.l_margin, pdf.get_y(), 2, 48, 'F')

        pdf.set_x(pdf.l_margin + 6)
        pdf.set_font('DVP', 'B', 8)
        pdf.set_text_color(*color)
        pdf.cell(pdf.get_string_width(region) + 8, 5, region)
        pdf.set_text_color(*pdf.SKY)
        pdf.cell(0, 5, proj_type, ln=True)

        # Title
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 11)
        pdf.cell(0, 6, title, ln=True)

        # Meta
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_text_color(*pdf.GRAY)
        pdf.set_font('DVP', 'I', 8)
        pdf.cell(0, 5, meta, ln=True)

        # Requirement
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_font('DVP', '', 8)
        pdf.set_text_color(180, 60, 60)
        pdf.multi_cell(160, 4.5, req)

        # Implementation
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_text_color(16, 130, 90)
        pdf.multi_cell(160, 4.5, impl)

        # Results
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 8)
        pdf.cell(0, 5, 'KET QUA: ' + results, ln=True)
        pdf.ln(6)

    # ═══ ĐỐI TÁC TIN CẬY ═══
    pdf.add_page()
    pdf.section_tag('ĐỐI TÁC TIN CẬY')
    pdf.section_title('Đối tác đã hợp tác')
    pdf.body_text(
        'Chúng tôi tự hào là đối tác tin cậy của các đơn vị tư vấn quy hoạch '
        'hàng đầu trên toàn quốc.'
    )

    partners = [
        'Viện QH Đô thị & Nông thôn Quốc gia',
        'Liên danh Tư vấn QH Phía Bắc',
        'Trung tâm Ứng dụng GIS TP.HCM',
        'Công ty CP QH Miền Trung',
        'Liên danh Tư vấn & ĐT Nam Việt',
        'Ban QLDA Hạ tầng Đô thị',
    ]
    for p in partners:
        pdf.set_fill_color(*pdf.LIGHT)
        y = pdf.get_y()
        pdf.rect(pdf.l_margin, y, 170, 8, 'F')
        pdf.set_fill_color(*pdf.BLUE)
        pdf.rect(pdf.l_margin, y, 2, 8, 'F')
        pdf.set_x(pdf.l_margin + 6)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 10)
        pdf.cell(0, 8, p, ln=True)
        pdf.ln(2)

    # ═══ ĐÁNH GIÁ TỪ ĐỐI TÁC ═══
    pdf.ln(5)
    pdf.section_tag('ĐÁNH GIÁ TỪ ĐỐI TÁC')
    pdf.section_title('Đối tác nói gì về chúng tôi?')

    testimonials = [
        ('"Giao hồ sơ CAD lúc 8 giờ tối, sáng hôm sau 7 giờ đã có GeoPackage hoàn chỉnh, '
         'quét 0 lỗi. Hội đồng thẩm định pass ngay lần đầu."',
         'Nguyễn Thanh Hùng',
         'GĐ Kỹ thuật - Công ty CP Tư vấn QH Miền Trung'),
        ('"Điểm tôi đánh giá cao nhất là đội ngũ biết rõ Thông tư 16 hơn cả chúng tôi. '
         'Họ chủ động phát hiện lỗi mà chúng tôi không biết là lỗi."',
         'Trần Thị Lan Anh',
         'Trưởng phòng GIS - Viện QH Đô thị và Nông thôn'),
        ('"Chính sách làm trước thanh toán sau là quyết định đúng đắn nhất. '
         'Đã hợp tác 5 gói thầu, chưa lần nào thất vọng."',
         'Phạm Đức Toàn',
         'Chủ tịch HĐQT - Liên danh Tư vấn QH Phía Nam'),
        ('"Tôi đã từng bị trả lại hồ sơ GIS 3 lần trước khi gặp GIS Quy Hoạch. '
         'Hợp đồng tiếp theo, pass ngay lần đầu và còn hỗ trợ giải trình thẩm định."',
         'Lê Quang Vinh',
         'KS trưởng - Ban QLDA huyện Điện Bàn'),
    ]
    for quote, name, role in testimonials:
        y = pdf.get_y()
        if y > 240:
            pdf.add_page()
        pdf.set_fill_color(248, 250, 252)
        pdf.rect(pdf.l_margin, y, 170, 1, 'F')
        pdf.ln(3)
        pdf.set_text_color(*pdf.GRAY)
        pdf.set_font('DVP', 'I', 9)
        pdf.multi_cell(165, 5, quote)
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 9)
        pdf.cell(0, 5, '  -- ' + name, ln=True)
        pdf.set_text_color(*pdf.SKY)
        pdf.set_font('DVP', '', 8)
        pdf.cell(0, 4, '     ' + role, ln=True)
        pdf.ln(5)

    # ═══ BẢNG GIÁ ═══
    pdf.add_page()
    pdf.section_tag('BẢNG GIÁ')
    pdf.section_title('Chi phí minh bạch, hợp lý')
    pdf.body_text(
        'Chúng tôi cam kết chính sách "Làm trước — Trả sau". '
        'Không yêu cầu đặt cọc. Thanh toán sau khi bạn kiểm tra và hài lòng.'
    )

    packages = [
        ('CƠ BẢN', '2 - 5 triệu', 'Hồ sơ quy mô nhỏ', [
            'Chuyển đổi CAD sang GIS',
            'Quét lỗi cơ bản',
            'GeoPackage chuẩn TT16',
            'Hỗ trợ thẩm định',
        ]),
        ('TIÊU CHUẨN', '5 - 15 triệu', 'Hồ sơ quy mô vừa', [
            'Tất cả tính năng Cơ bản',
            'WebGIS viewer',
            'Quét lỗi nâng cao',
            'Đồng hành thẩm định',
            'Báo cáo kiểm tra chất lượng',
        ]),
        ('TOÀN DIỆN', 'Theo thỏa thuận', 'Hồ sơ lớn / phức tạp', [
            'Tất cả tính năng Tiêu chuẩn',
            'Hồ sơ dự thầu GIS',
            'Hỗ trợ nghiệm thu',
            'Đồng hành toàn gói thầu',
        ]),
    ]

    col_w = 55
    gap = 3
    start_x = (210 - (col_w * 3 + gap * 2)) / 2
    y_start = pdf.get_y() + 2

    for i, (tier, price, sub, features) in enumerate(packages):
        x = start_x + i * (col_w + gap)
        # Card background
        is_featured = (i == 1)
        if is_featured:
            pdf.set_fill_color(240, 249, 255)
        else:
            pdf.set_fill_color(*pdf.LIGHT)
        pdf.rect(x, y_start, col_w, 90, 'F')

        # Header
        if is_featured:
            pdf.set_fill_color(*pdf.BLUE)
        else:
            pdf.set_fill_color(*pdf.SKY)
        pdf.rect(x, y_start, col_w, 14, 'F')
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('DVP', 'B', 10)
        pdf.set_xy(x, y_start + 3)
        pdf.cell(col_w, 8, tier, align='C')

        # Price
        pdf.set_text_color(*pdf.DARK)
        pdf.set_font('DVP', 'B', 13)
        pdf.set_xy(x, y_start + 18)
        pdf.cell(col_w, 8, price, align='C')

        pdf.set_text_color(*pdf.GRAY)
        pdf.set_font('DVP', '', 8)
        pdf.set_xy(x, y_start + 27)
        pdf.cell(col_w, 5, sub, align='C')

        # Features
        fy = y_start + 38
        for feat in features:
            pdf.set_text_color(*pdf.GRAY)
            pdf.set_font('DVP', '', 8)
            pdf.set_xy(x + 4, fy)
            pdf.cell(col_w - 8, 5, '✓ ' + feat)
            fy += 8

    pdf.set_y(y_start + 98)

    # ═══ LIÊN HỆ ═══
    pdf.ln(10)
    y = pdf.get_y()
    pdf.set_fill_color(*pdf.BLUE)
    pdf.rect(pdf.l_margin, y, 170, 55, 'F')

    pdf.set_text_color(255, 255, 255)
    pdf.set_font('DVP', 'B', 16)
    pdf.set_xy(pdf.l_margin, y + 8)
    pdf.cell(170, 8, 'Liên hệ tư vấn miễn phí', align='C', ln=True)

    pdf.set_font('DVP', '', 10)
    pdf.set_text_color(200, 220, 255)
    pdf.cell(170, 6, 'Gửi hồ sơ — Nhận báo giá trong 2 giờ — Làm trước trả sau', align='C', ln=True)

    pdf.ln(5)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('DVP', 'B', 12)
    pdf.cell(170, 7, '📞  0332 945 089    |    💬  Zalo: 0332 945 089', align='C', ln=True)
    pdf.cell(170, 7, '📘  fb.com/Gisquyhoach', align='C', ln=True)

    # ═══ FOOTER ═══
    pdf.set_y(280)
    pdf.set_text_color(150, 150, 150)
    pdf.set_font('DVP', 'I', 8)
    pdf.cell(0, 5, 'GIS Quy Hoạch — Hồ Sơ Năng Lực 2025 — Hotline: 0332 945 089', align='C')

    # Save
    out_path = os.path.join(os.path.dirname(__file__), 'Ho_So_Nang_Luc_GIS_Quy_Hoach.pdf')
    pdf.output(out_path)
    print(f'PDF saved: {out_path}')


if __name__ == '__main__':
    build_pdf()
