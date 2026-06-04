-- ══════════════════════════════════════════════════════════════
-- WEBGIS PORTAL SCHEMA — GIS Quy Hoạch
-- Chạy script này trong Supabase SQL Editor
-- ══════════════════════════════════════════════════════════════

-- 1. Bảng dự án
CREATE TABLE IF NOT EXISTS projects (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name        TEXT NOT NULL,
  client_name TEXT NOT NULL,
  description TEXT,
  access_code TEXT NOT NULL,        -- Mã truy cập riêng cho khách
  status      TEXT DEFAULT 'active' CHECK (status IN ('active','archived')),
  created_at  TIMESTAMPTZ DEFAULT now(),
  updated_at  TIMESTAMPTZ DEFAULT now()
);

-- 2. Bảng file GIS của từng dự án
CREATE TABLE IF NOT EXISTS project_files (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id   UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  display_name TEXT NOT NULL,       -- Tên lớp hiển thị (VD: "Ranh giới chức năng")
  storage_path TEXT NOT NULL,       -- Đường dẫn trong Supabase Storage
  layer_color  TEXT DEFAULT '#3b82f6',
  layer_type   TEXT DEFAULT 'polygon' CHECK (layer_type IN ('polygon','line','point')),
  visible      BOOLEAN DEFAULT true,
  sort_order   INT DEFAULT 0,
  created_at   TIMESTAMPTZ DEFAULT now()
);

-- 3. RLS Policies
ALTER TABLE projects      ENABLE ROW LEVEL SECURITY;
ALTER TABLE project_files ENABLE ROW LEVEL SECURITY;

-- Chỉ authenticated user (admin) có thể INSERT/UPDATE/DELETE
CREATE POLICY "admin_all_projects" ON projects
  FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "admin_all_files" ON project_files
  FOR ALL USING (auth.role() = 'authenticated');

-- Public có thể SELECT projects và project_files (frontend check access_code)
CREATE POLICY "public_read_projects" ON projects
  FOR SELECT USING (status = 'active');

CREATE POLICY "public_read_files" ON project_files
  FOR SELECT USING (true);

-- 4. Supabase Storage — TẠO BUCKET thủ công trong Dashboard:
-- Storage → New Bucket → Name: "gis-files" → Public: TRUE
-- Sau đó thêm Policy: Allow public downloads (GET)
-- Policy for upload (INSERT): auth.role() = 'authenticated'

-- 5. Index
CREATE INDEX IF NOT EXISTS idx_project_files_project_id ON project_files(project_id);
CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status);
