-- ==============================================================================
-- KỊCH BẢN TẠO CƠ SỞ DỮ LIỆU SUPABASE CHO HỆ THỐNG KHÓA HỌC GIS
-- Copy toàn bộ nội dung này và dán vào mục "SQL Editor" trên Supabase
-- ==============================================================================

-- 1. Tạo bảng Danh sách khóa học (Courses)
CREATE TABLE IF NOT EXISTS public.courses (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  title text NOT NULL,
  description text,
  thumbnail_url text,
  price numeric DEFAULT 0,
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Tạo bảng Bài giảng (Videos/Lessons)
CREATE TABLE IF NOT EXISTS public.lessons (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  course_id uuid REFERENCES public.courses(id) ON DELETE CASCADE,
  title text NOT NULL,
  video_path text NOT NULL, -- Đường dẫn file trong Storage (VD: video-arcgis-quy-hoach/bai-1.mp4)
  order_index integer NOT NULL, -- Thứ tự bài học
  is_free boolean DEFAULT false, -- Bài học miễn phí (học thử)?
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 3. Tạo bảng Quyền truy cập Khóa học (Course Enrollments)
-- Lưu trữ thông tin user nào đã mua khóa học nào
CREATE TABLE IF NOT EXISTS public.enrollments (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE,
  course_id uuid REFERENCES public.courses(id) ON DELETE CASCADE,
  enrolled_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  UNIQUE(user_id, course_id)
);

-- ==============================================================================
-- CẤU HÌNH BẢO MẬT (ROW LEVEL SECURITY - RLS)
-- ==============================================================================

-- Kích hoạt RLS
ALTER TABLE public.courses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.lessons ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.enrollments ENABLE ROW LEVEL SECURITY;

-- Chính sách: Bất kỳ ai cũng có thể xem danh sách khóa học
CREATE POLICY "Cho phép xem danh sách khóa học" 
  ON public.courses FOR SELECT USING (true);

-- Chính sách: Bất kỳ ai cũng có thể xem danh sách bài giảng
CREATE POLICY "Cho phép xem danh sách bài giảng" 
  ON public.lessons FOR SELECT USING (true);

-- Chính sách: Người dùng chỉ được xem thông tin ghi danh của chính mình
CREATE POLICY "Chỉ xem khóa đã mua của mình" 
  ON public.enrollments FOR SELECT 
  USING (auth.uid() = user_id);

-- ==============================================================================
-- BẢO MẬT STORAGE (FILE VIDEO)
-- Yêu cầu: Bạn phải tạo trước một Bucket tên là 'courses' trong mục Storage
-- ==============================================================================

-- Chính sách: Chỉ cho phép tải file (chọn SELECT) nếu user đã đăng nhập
-- VÀ user đó đã mua khóa học chứa file video này.
CREATE POLICY "Chỉ học viên đã mua mới được tải video"
  ON storage.objects FOR SELECT
  USING (
    bucket_id = 'courses' AND
    auth.role() = 'authenticated'
  );
