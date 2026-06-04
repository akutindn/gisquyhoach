-- =============================================
-- BƯỚC 1: Tạo bảng courses (Khóa học)
-- =============================================
CREATE TABLE IF NOT EXISTS public.courses (
    id TEXT PRIMARY KEY,          -- 'arcgis', 'qgis'
    name TEXT NOT NULL,           -- 'ARCGIS', 'QGIS'
    full_name TEXT NOT NULL,      -- 'Khóa học TT16 (ArcGIS)'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- =============================================
-- BƯỚC 2: Tạo bảng lessons (Bài học)
-- =============================================
CREATE TABLE IF NOT EXISTS public.lessons (
    id SERIAL PRIMARY KEY,
    course_id TEXT REFERENCES public.courses(id),
    lesson_order INT NOT NULL,
    title TEXT NOT NULL,
    duration TEXT NOT NULL,
    drive_id TEXT NOT NULL,       -- ID file Google Drive (ẩn khỏi frontend)
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- =============================================
-- BƯỚC 3: Bật Row Level Security (RLS) - QUAN TRỌNG!
-- =============================================
ALTER TABLE public.courses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.lessons ENABLE ROW LEVEL SECURITY;

-- Chỉ user đã đăng nhập mới đọc được
CREATE POLICY "Authenticated users can read courses"
    ON public.courses FOR SELECT
    TO authenticated
    USING (true);

CREATE POLICY "Authenticated users can read lessons"
    ON public.lessons FOR SELECT
    TO authenticated
    USING (true);

-- Chặn hoàn toàn user vô danh (anon)
CREATE POLICY "Block anon from courses"
    ON public.courses FOR ALL
    TO anon
    USING (false);

CREATE POLICY "Block anon from lessons"
    ON public.lessons FOR ALL
    TO anon
    USING (false);

-- =============================================
-- BƯỚC 4: Nhập dữ liệu khóa học
-- =============================================
INSERT INTO public.courses (id, name, full_name) VALUES
    ('arcgis', 'ARCGIS', 'Khóa học TT16 (ArcGIS)'),
    ('qgis', 'QGIS', 'Khóa học TT16 (QGIS)')
ON CONFLICT (id) DO NOTHING;

INSERT INTO public.lessons (course_id, lesson_order, title, duration, drive_id) VALUES
    -- ArcGIS
    ('arcgis', 1, 'Bài 1: Chuyển đổi bản đồ địa hình, quy hoạch sang định dạng GIS', '15 Phút', '1vanOVqxwtdpi0sMLKCI1pnYsDXlDjvA7'),
    ('arcgis', 2, 'Bài 2: Biên tập dữ liệu không gian cho từng lớp',                 '20 Phút', '1qL-U2NPIz2oTFHk_tDqwg75JaAckd1Ol'),
    ('arcgis', 3, 'Bài 3: Biên tập dữ liệu thuộc tính cho từng lớp',                 '25 Phút', '1en1L6rnQ3bYxDOHQbutilxtI9ni2TCQL'),
    ('arcgis', 4, 'Bài 4: Thiết kế kí hiệu cho từng lớp',                            '18 Phút', '1n6mDJy8May7OxoRXbzZ3JIMQQx6QK2lH'),
    ('arcgis', 5, 'Bài 5: Đóng gói cơ sở dữ liệu số địa lý',                        '22 Phút', '1ncpgUE4nPhYWF9KXodeQKR8RBIeRfkCD'),
    -- QGIS
    ('qgis',   1, 'Bài 1: Tổng quan QGIS',                                            '20 Phút', '1uQI0XAekvrjePSdu3KMRLLpam4RD419Y'),
    ('qgis',   2, 'Bài 2: Hệ tọa độ & Công cụ biên tập',                             '25 Phút', '1FvDmqKdYuwLBIDkcelC1LRS0wq4ctf6f'),
    ('qgis',   3, 'Bài 3: Xử lý dữ liệu CAD',                                        '22 Phút', '1fGpqXckR5e7wIJd3px7HD0mM6f0cGuNc'),
    ('qgis',   4, 'Bài 4: Bản đồ chuyên đề & Bố cục in',                             '20 Phút', '1Vdxu1QJjxhDaPT3R5EsmjNn8h8zC8_BL')
ON CONFLICT DO NOTHING;
