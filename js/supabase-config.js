// Cấu hình kết nối Supabase
// HƯỚNG DẪN: Thay thế 2 biến dưới đây bằng thông tin thực tế từ tài khoản Supabase của bạn.
const SUPABASE_URL = 'VUI_LONG_NHAP_SUPABASE_URL_VAO_DAY';
const SUPABASE_ANON_KEY = 'VUI_LONG_NHAP_SUPABASE_ANON_KEY_VAO_DAY';

// Khởi tạo client Supabase
let supabase = null;

if (typeof window.supabase !== 'undefined' && SUPABASE_URL !== 'VUI_LONG_NHAP_SUPABASE_URL_VAO_DAY') {
    supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
} else {
    console.warn("⚠️ Chưa cấu hình Supabase API Key hoặc thư viện chưa được nạp!");
}

// Các hàm tiện ích
async function checkLogin() {
    if (!supabase) return null;
    const { data: { user } } = await supabase.auth.getUser();
    return user;
}
