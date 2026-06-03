// Cấu hình kết nối Supabase
// HƯỚNG DẪN: Thay thế 2 biến dưới đây bằng thông tin thực tế từ tài khoản Supabase của bạn.
const SUPABASE_URL = 'https://sscoxcaexukcklamdzyu.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_5PymJjG2K_jNJm0uOFnhTQ_sQNI2_Db';

// Khởi tạo client Supabase
let supabaseClient = null;

if (typeof window.supabase !== 'undefined' && SUPABASE_URL !== 'VUI_LONG_NHAP_SUPABASE_URL_VAO_DAY') {
    supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
} else {
    console.warn("⚠️ Chưa cấu hình Supabase API Key hoặc thư viện chưa được nạp!");
}

// Các hàm tiện ích
async function checkLogin() {
    if (!supabaseClient) return null;
    const { data: { user } } = await supabaseClient.auth.getUser();
    return user;
}
