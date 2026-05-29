# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.abspath(__file__))

HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>GisVN — Lập hồ sơ quy hoạch trên GIS chuyên nghiệp</title>
<meta name="description" content="Đối tác tin cậy cho hạng mục GIS trong lập hồ sơ quy hoạch. Tuân thủ Thông tư 16, hoàn thành 1-3 ngày, làm trước thanh toán sau."/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet"/>
<style>
:root{
  --bg:#050b18;--bg2:#080f1e;--surface:rgba(255,255,255,.04);--glass:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08);--text:#f0f4ff;--muted:#8892a4;--dim:#4a5568;
  --primary:#0ea5e9;--pl:#38bdf8;--accent:#10b981;--warn:#f59e0b;--danger:#ef4444;
  --grad:linear-gradient(135deg,#0ea5e9,#6366f1);
  --shadow:0 24px 64px rgba(0,0,0,.5);--radius:14px;--radiuslg:20px;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Be Vietnam Pro',sans-serif;background:var(--bg);color:var(--text);overflow-x:hidden;line-height:1.6;}
a{text-decoration:none;color:inherit;}
img{max-width:100%;}

/* ── Buttons ── */
.btn{display:inline-flex;align-items:center;gap:8px;padding:13px 28px;border-radius:12px;font-family:inherit;font-weight:700;font-size:15px;cursor:pointer;border:none;transition:all .25s;white-space:nowrap;}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 8px 24px rgba(14,165,233,.35);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(14,165,233,.5);}
.btn-outline{background:transparent;border:1.5px solid var(--border);color:var(--text);}
.btn-outline:hover{background:var(--glass);border-color:var(--primary);}
.btn-xl{padding:17px 40px;font-size:17px;border-radius:14px;}
.btn-green{background:linear-gradient(135deg,#10b981,#059669);color:#fff;box-shadow:0 8px 24px rgba(16,185,129,.35);}
.btn-green:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(16,185,129,.5);}

/* ── Navbar ── */
.navbar{position:fixed;top:0;left:0;right:0;z-index:999;padding:0 40px;height:70px;display:flex;align-items:center;background:rgba(5,11,24,.8);backdrop-filter:blur(20px);border-bottom:1px solid transparent;transition:all .3s;}
.navbar.scrolled{border-bottom-color:var(--border);}
.nav-inner{max-width:1200px;margin:0 auto;width:100%;display:flex;align-items:center;gap:32px;}
.logo{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:900;}
.logo-icon{width:38px;height:38px;background:var(--grad);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;}
.logo span.accent{color:var(--pl);}
.nav-links{display:flex;gap:4px;margin-left:auto;}
.nav-link{padding:8px 16px;border-radius:8px;font-size:14px;font-weight:600;color:var(--muted);transition:all .2s;}
.nav-link:hover{color:var(--text);background:var(--glass);}
.nav-cta{margin-left:12px;}

/* ── Hero ── */
.hero{min-height:100vh;display:flex;align-items:center;position:relative;overflow:hidden;padding:100px 40px 60px;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(14,165,233,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(14,165,233,.06) 1px,transparent 1px);background-size:60px 60px;mask-image:radial-gradient(ellipse 80% 60% at 50% 30%,black,transparent);}
.orb{position:absolute;border-radius:50%;filter:blur(80px);opacity:.4;animation:float 8s ease-in-out infinite;}
.orb-1{width:500px;height:500px;background:radial-gradient(circle,#0ea5e9,transparent);top:-150px;right:-100px;animation-delay:0s;}
.orb-2{width:400px;height:400px;background:radial-gradient(circle,#6366f1,transparent);bottom:-100px;left:-80px;animation-delay:-3s;}
.orb-3{width:300px;height:300px;background:radial-gradient(circle,#10b981,transparent);top:40%;right:20%;animation-delay:-5s;opacity:.25;}
@keyframes float{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(20px,-30px) scale(1.05);}}
.hero-inner{max-width:1200px;margin:0 auto;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:1;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(14,165,233,.12);border:1px solid rgba(14,165,233,.25);border-radius:100px;padding:6px 16px 6px 8px;font-size:13px;font-weight:700;color:var(--pl);margin-bottom:24px;}
.badge-dot{width:8px;height:8px;background:var(--accent);border-radius:50%;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.6;transform:scale(1.4);}}
.hero-title{font-size:52px;font-weight:900;line-height:1.15;margin-bottom:20px;}
.hero-title .line-accent{background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hero-desc{font-size:17px;color:var(--muted);line-height:1.8;margin-bottom:32px;max-width:520px;}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:44px;}
.hero-stats{display:flex;gap:32px;}
.hstat{text-align:center;}
.hstat-num{font-size:28px;font-weight:900;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hstat-lbl{font-size:12px;color:var(--muted);font-weight:600;}

/* GIS Visual */
.hero-visual{position:relative;}
.gis-card{background:rgba(8,15,30,.9);backdrop-filter:blur(20px);border:1px solid var(--border);border-radius:20px;overflow:hidden;box-shadow:0 40px 80px rgba(0,0,0,.5);}
.gis-topbar{background:rgba(255,255,255,.04);border-bottom:1px solid var(--border);padding:12px 20px;display:flex;align-items:center;gap:10px;}
.gis-dots span{width:12px;height:12px;border-radius:50%;display:inline-block;margin-right:6px;}
.gis-dots span:nth-child(1){background:#ff5f57;}
.gis-dots span:nth-child(2){background:#febc2e;}
.gis-dots span:nth-child(3){background:#28c840;}
.gis-title-bar{font-size:13px;color:var(--muted);font-weight:600;}
.gis-body{padding:20px;}
.gis-map{background:rgba(14,165,233,.05);border:1px solid rgba(14,165,233,.15);border-radius:12px;height:200px;position:relative;overflow:hidden;margin-bottom:16px;}
.map-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(14,165,233,.1) 1px,transparent 1px),linear-gradient(90deg,rgba(14,165,233,.1) 1px,transparent 1px);background-size:24px 24px;}
.map-polygon{position:absolute;top:30px;left:40px;width:120px;height:80px;background:rgba(14,165,233,.2);border:2px solid var(--primary);border-radius:4px;animation:blink-border 3s infinite;}
.map-polygon2{position:absolute;top:60px;left:180px;width:80px;height:100px;background:rgba(16,185,129,.15);border:2px solid var(--accent);border-radius:4px;}
.map-polygon3{position:absolute;top:20px;left:300px;width:60px;height:60px;background:rgba(245,158,11,.15);border:2px solid var(--warn);border-radius:4px;}
.map-point{position:absolute;width:10px;height:10px;border-radius:50%;background:var(--primary);box-shadow:0 0 12px var(--primary);}
@keyframes blink-border{0%,100%{border-color:var(--primary);}50%{border-color:var(--pl);box-shadow:0 0 20px rgba(14,165,233,.4);}}
.map-label{position:absolute;font-size:10px;font-family:'Fira Code',monospace;color:var(--pl);background:rgba(14,165,233,.1);padding:2px 6px;border-radius:4px;}
.gis-layers{display:flex;flex-direction:column;gap:8px;}
.layer-row{display:flex;align-items:center;gap:10px;padding:8px 12px;background:rgba(255,255,255,.03);border-radius:8px;font-size:13px;}
.layer-color{width:14px;height:14px;border-radius:3px;flex-shrink:0;}
.layer-name{flex:1;font-weight:600;}
.layer-status{font-size:11px;padding:2px 8px;border-radius:10px;font-weight:700;}
.ls-ok{background:rgba(16,185,129,.15);color:#10b981;}
.ls-proc{background:rgba(14,165,233,.15);color:#38bdf8;animation:blink-text 1.5s infinite;}
@keyframes blink-text{0%,100%{opacity:1;}50%{opacity:.5;}}
.gis-progress-bar{margin-top:14px;background:rgba(255,255,255,.06);border-radius:100px;height:6px;overflow:hidden;}
.gis-progress-fill{height:100%;background:var(--grad);border-radius:100px;width:75%;animation:progress-anim 3s ease-in-out infinite;}
@keyframes progress-anim{0%{width:60%;}50%{width:85%;}100%{width:60%;}}
.gis-footer-bar{display:flex;justify-content:space-between;align-items:center;margin-top:12px;font-size:12px;color:var(--muted);}
.floating-badge{position:absolute;background:rgba(8,15,30,.95);border:1px solid var(--border);border-radius:12px;padding:10px 14px;font-size:13px;font-weight:700;box-shadow:0 8px 24px rgba(0,0,0,.4);}
.fb1{bottom:-20px;left:-30px;color:var(--accent);}
.fb2{top:-20px;right:-20px;color:var(--warn);}
.fb3{bottom:40px;right:-50px;color:var(--pl);}

/* ── Pain section ── */
.section{padding:100px 40px;}
.container{max-width:1200px;margin:0 auto;}
.sec-tag{display:inline-block;background:rgba(14,165,233,.1);border:1px solid rgba(14,165,233,.2);color:var(--pl);font-size:12px;font-weight:800;padding:5px 14px;border-radius:100px;text-transform:uppercase;letter-spacing:.08em;margin-bottom:16px;}
.sec-title{font-size:40px;font-weight:900;line-height:1.2;margin-bottom:16px;}
.sec-desc{font-size:17px;color:var(--muted);max-width:600px;line-height:1.8;}

.pain-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:48px;}
.pain-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radiuslg);padding:28px;position:relative;overflow:hidden;transition:all .3s;}
.pain-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(239,68,68,.06),transparent);opacity:0;transition:opacity .3s;}
.pain-card:hover{border-color:rgba(239,68,68,.3);transform:translateY(-4px);}
.pain-card:hover::before{opacity:1;}
.pain-icon{font-size:32px;margin-bottom:14px;}
.pain-card h3{font-size:18px;font-weight:800;margin-bottom:10px;}
.pain-card p{color:var(--muted);font-size:15px;line-height:1.7;}
.pain-quote{background:linear-gradient(135deg,rgba(14,165,233,.08),rgba(99,102,241,.08));border:1px solid rgba(14,165,233,.2);border-radius:var(--radiuslg);padding:40px;margin-top:48px;text-align:center;}
.pain-quote blockquote{font-size:20px;font-weight:700;line-height:1.7;color:var(--text);font-style:italic;}
.pain-quote cite{display:block;margin-top:16px;color:var(--pl);font-size:14px;font-weight:700;font-style:normal;}

/* ── Features / USP ── */
.sec-dark{background:var(--bg2);}
.features-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:56px;}
.feat-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radiuslg);padding:28px 24px;transition:all .3s;position:relative;overflow:hidden;}
.feat-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--grad);transform:scaleX(0);transform-origin:left;transition:transform .3s;}
.feat-card:hover{transform:translateY(-6px);border-color:rgba(14,165,233,.3);box-shadow:0 20px 40px rgba(0,0,0,.3);}
.feat-card:hover::after{transform:scaleX(1);}
.feat-icon{width:52px;height:52px;border-radius:14px;background:rgba(14,165,233,.12);display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:18px;}
.feat-card h3{font-size:17px;font-weight:800;margin-bottom:10px;}
.feat-card p{color:var(--muted);font-size:14px;line-height:1.7;}

/* ── Process ── */
.process-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:64px;position:relative;}
.process-steps::before{content:'';position:absolute;top:36px;left:12.5%;right:12.5%;height:2px;background:linear-gradient(90deg,var(--primary),var(--accent));z-index:0;}
.step{text-align:center;padding:0 16px;position:relative;z-index:1;}
.step-num{width:72px;height:72px;border-radius:50%;margin:0 auto 20px;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:900;border:3px solid;position:relative;background:var(--bg);}
.sn1{border-color:var(--primary);color:var(--primary);box-shadow:0 0 24px rgba(14,165,233,.3);}
.sn2{border-color:#818cf8;color:#818cf8;box-shadow:0 0 24px rgba(129,140,248,.3);}
.sn3{border-color:var(--warn);color:var(--warn);box-shadow:0 0 24px rgba(245,158,11,.3);}
.sn4{border-color:var(--accent);color:var(--accent);box-shadow:0 0 24px rgba(16,185,129,.3);}
.step h4{font-size:16px;font-weight:800;margin-bottom:8px;}
.step p{font-size:13px;color:var(--muted);line-height:1.6;}

/* ── Commitments ── */
.commit-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:48px;}
.commit-item{display:flex;gap:16px;align-items:flex-start;padding:22px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);transition:all .25s;}
.commit-item:hover{border-color:rgba(16,185,129,.3);background:rgba(16,185,129,.04);}
.commit-icon{width:44px;height:44px;border-radius:12px;background:rgba(16,185,129,.12);display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0;}
.commit-item h4{font-size:15px;font-weight:800;margin-bottom:6px;}
.commit-item p{font-size:13px;color:var(--muted);line-height:1.6;}

/* ── Standards ── */
.std-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-top:56px;}
.std-list{display:flex;flex-direction:column;gap:14px;}
.std-item{display:flex;align-items:center;gap:14px;padding:16px 20px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);}
.std-badge{font-size:11px;font-weight:800;padding:4px 10px;border-radius:6px;white-space:nowrap;}
.sb-blue{background:rgba(14,165,233,.15);color:#38bdf8;}
.sb-green{background:rgba(16,185,129,.15);color:#10b981;}
.sb-purple{background:rgba(99,102,241,.15);color:#818cf8;}
.std-item p{font-size:14px;font-weight:600;}
.std-visual{background:rgba(8,15,30,.8);border:1px solid var(--border);border-radius:var(--radiuslg);padding:28px;font-family:'Fira Code',monospace;font-size:13px;line-height:2;}
.sv-comment{color:#4a5568;}
.sv-key{color:#38bdf8;}
.sv-val{color:#10b981;}
.sv-str{color:#f59e0b;}
.sv-num{color:#c084fc;}

/* ── CTA / Contact ── */
.cta-section{padding:100px 40px;position:relative;overflow:hidden;}
.cta-bg{position:absolute;inset:0;background:linear-gradient(135deg,rgba(14,165,233,.08),rgba(99,102,241,.08));z-index:0;}
.contact-card{background:rgba(8,15,30,.9);backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:24px;padding:60px;max-width:800px;margin:0 auto;position:relative;z-index:1;box-shadow:var(--shadow);}
.contact-card h2{font-size:36px;font-weight:900;text-align:center;margin-bottom:12px;}
.contact-card .sub{text-align:center;color:var(--muted);margin-bottom:44px;font-size:16px;}
.contact-form{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.form-group{display:flex;flex-direction:column;gap:7px;}
.form-group.full{grid-column:1/-1;}
.form-group label{font-size:13px;font-weight:700;color:var(--muted);}
.form-group input,.form-group textarea,.form-group select{background:rgba(255,255,255,.05);border:1.5px solid var(--border);border-radius:10px;padding:13px 16px;color:var(--text);font-family:'Be Vietnam Pro',sans-serif;font-size:14px;outline:none;transition:all .2s;resize:none;}
.form-group input:focus,.form-group textarea:focus,.form-group select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(14,165,233,.15);}
.form-group select option{background:#080f1e;}
.form-submit{grid-column:1/-1;text-align:center;margin-top:8px;}
.contact-direct{display:flex;justify-content:center;gap:32px;margin-top:32px;flex-wrap:wrap;}
.cd-item{display:flex;align-items:center;gap:10px;font-size:15px;font-weight:700;}
.cd-icon{font-size:22px;}

/* ── Footer ── */
.footer{background:var(--bg2);border-top:1px solid var(--border);padding:48px 40px 32px;}
.footer-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr;gap:48px;}
.footer-logo{font-size:20px;font-weight:900;margin-bottom:14px;}
.footer-desc{color:var(--muted);font-size:14px;line-height:1.8;max-width:320px;}
.footer-col h4{font-size:14px;font-weight:800;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin-bottom:16px;}
.footer-links{display:flex;flex-direction:column;gap:10px;}
.footer-links a{color:var(--muted);font-size:14px;transition:color .2s;}
.footer-links a:hover{color:var(--pl);}
.footer-bottom{max-width:1200px;margin:32px auto 0;padding-top:24px;border-top:1px solid var(--border);display:flex;justify-content:space-between;font-size:13px;color:var(--dim);}

/* ── Responsive ── */
@media(max-width:900px){
  .hero-inner{grid-template-columns:1fr;}
  .hero-visual{display:none;}
  .hero-title{font-size:36px;}
  .pain-grid,.features-grid,.commit-grid,.std-wrap,.footer-inner{grid-template-columns:1fr;}
  .contact-form{grid-template-columns:1fr;}
  .process-steps{grid-template-columns:1fr 1fr;}
  .process-steps::before{display:none;}
  .navbar{padding:0 20px;}
  .section,.hero,.cta-section{padding:70px 20px;}
}
</style>
</head>
<body>

<!-- ══ NAVBAR ══════════════════════════════════════════════ -->
<nav class="navbar" id="navbar">
  <div class="nav-inner">
    <div class="logo">
      <div class="logo-icon">🗺</div>
      <span>GIS<span class="accent">VN</span></span>
    </div>
    <div class="nav-links">
      <a href="#pain"     class="nav-link">Vấn đề hiện tại</a>
      <a href="#features" class="nav-link">Dịch vụ</a>
      <a href="#process"  class="nav-link">Quy trình</a>
      <a href="#standards"class="nav-link">Tiêu chuẩn</a>
    </div>
    <a href="#contact" class="btn btn-primary nav-cta">Liên hệ ngay</a>
  </div>
</nav>

<!-- ══ HERO ════════════════════════════════════════════════ -->
<section class="hero" id="home">
  <div class="hero-bg">
    <div class="hero-grid"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-badge"><span class="badge-dot"></span>Tuân thủ Thông tư 16 · Chuẩn GIS quốc gia</div>
      <h1 class="hero-title">
        Đối tác <span class="line-accent">GIS chuyên nghiệp</span><br/>
        cho hồ sơ quy hoạch<br/>của bạn
      </h1>
      <p class="hero-desc">
        Từ quy hoạch sử dụng đất đến xây dựng, giao thông — chúng tôi chuyển đổi toàn bộ hồ sơ CAD sang cơ sở dữ liệu GIS chuẩn Thông tư 16, hoàn thành trong <strong>1–3 ngày làm việc</strong>.
      </p>
      <div class="hero-actions">
        <a href="#contact" class="btn btn-primary btn-xl">📞 Liên hệ tư vấn miễn phí</a>
        <a href="#process" class="btn btn-outline btn-xl">Xem quy trình →</a>
      </div>
      <div class="hero-stats">
        <div class="hstat"><div class="hstat-num">100%</div><div class="hstat-lbl">Tuân thủ TT16</div></div>
        <div class="hstat"><div class="hstat-num">1–3</div><div class="hstat-lbl">Ngày hoàn thành</div></div>
        <div class="hstat"><div class="hstat-num">0đ</div><div class="hstat-lbl">Trả trước</div></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="gis-card">
        <div class="gis-topbar">
          <div class="gis-dots"><span></span><span></span><span></span></div>
          <div class="gis-title-bar">🗺 GIS Viewer — Hồ sơ quy hoạch TP. Đà Nẵng</div>
        </div>
        <div class="gis-body">
          <div class="gis-map">
            <div class="map-grid"></div>
            <div class="map-polygon"><span class="map-label" style="top:8px;left:8px;">ODT</span></div>
            <div class="map-polygon2"><span class="map-label" style="top:8px;left:4px">CXD</span></div>
            <div class="map-polygon3"><span class="map-label" style="top:6px;left:4px">GT</span></div>
            <div class="map-point" style="top:110px;left:250px"></div>
            <div class="map-point" style="top:50px;left:380px;background:var(--accent);box-shadow:0 0 12px var(--accent)"></div>
          </div>
          <div class="gis-layers">
            <div class="layer-row"><div class="layer-color" style="background:#0ea5e9"></div><span class="layer-name">Đất ở đô thị (ODT)</span><span class="layer-status ls-ok">✓ Chuẩn</span></div>
            <div class="layer-row"><div class="layer-color" style="background:#10b981"></div><span class="layer-name">Công trình XD (CXD)</span><span class="layer-status ls-ok">✓ Chuẩn</span></div>
            <div class="layer-row"><div class="layer-color" style="background:#f59e0b"></div><span class="layer-name">Giao thông (GT)</span><span class="layer-status ls-proc">⟳ Đang xử lý...</span></div>
          </div>
          <div class="gis-progress-bar"><div class="gis-progress-fill"></div></div>
          <div class="gis-footer-bar"><span>Tiến trình: Quét lỗi topology...</span><span style="color:var(--accent)">✓ 32 lớp OK</span></div>
        </div>
      </div>
      <div class="floating-badge fb1">✅ Quét lỗi tự động</div>
      <div class="floating-badge fb2">⚡ EPSG:5897 · VN2000</div>
      <div class="floating-badge fb3">📦 GeoPackage chuẩn</div>
    </div>
  </div>
</section>

<!-- ══ PAIN POINTS ══════════════════════════════════════════ -->
<section class="section sec-dark" id="pain">
  <div class="container">
    <div class="sec-tag">Bức tranh hiện tại</div>
    <h2 class="sec-title">Doanh nghiệp của bạn đang<br/>gặp phải điều này?</h2>
    <p class="sec-desc">GIS đã trở thành yêu cầu bắt buộc trong 100% gói thầu lập quy hoạch — nhưng không phải ai cũng sẵn sàng.</p>
    <div class="pain-grid">
      <div class="pain-card">
        <div class="pain-icon">📌</div>
        <h3>GIS bắt buộc trong 100% gói thầu</h3>
        <p>Các tỉnh/thành phố đã chỉ đạo đưa ứng dụng GIS vào toàn bộ hồ sơ quy hoạch, nhưng đội ngũ nội bộ chưa có đủ năng lực thực hiện.</p>
      </div>
      <div class="pain-card">
        <div class="pain-icon">📋</div>
        <h3>Hiểu sai về Thông tư 16</h3>
        <p>TT16 quy định GIS phải <strong>song hành từ đầu đến cuối</strong> gói thầu — không phải chỉ đơn giản là chuyển đổi file CAD sang GIS sau khi phê duyệt.</p>
      </div>
      <div class="pain-card">
        <div class="pain-icon">⏰</div>
        <h3>Áp lực thời hạn thẩm định</h3>
        <p>Hồ sơ GIS không kịp tiến độ dẫn đến chậm trình thẩm định, ảnh hưởng trực tiếp đến tiến độ toàn bộ dự án và uy tín doanh nghiệp.</p>
      </div>
      <div class="pain-card">
        <div class="pain-icon">🔍</div>
        <h3>Lỗi dữ liệu không được kiểm soát</h3>
        <p>Hồ sơ GIS tự làm thường có lỗi topology, sai hệ tọa độ, thiếu trường thuộc tính — bị trả về nhiều lần khi thẩm định.</p>
      </div>
    </div>
    <div class="pain-quote">
      <blockquote>"Việc lập quy hoạch trên GIS là một hạng mục song hành từ đầu đến cuối cùng với việc lập quy hoạch, chứ không đơn thuần là chuyển đổi file sản phẩm đã được phê duyệt từ CAD sang GIS."</blockquote>
      <cite>— Thông tư 16/BXD · Quy định về lập hồ sơ quy hoạch trên nền tảng GIS</cite>
    </div>
  </div>
</section>

<!-- ══ FEATURES ═════════════════════════════════════════════ -->
<section class="section" id="features">
  <div class="container">
    <div class="sec-tag">Dịch vụ của chúng tôi</div>
    <h2 class="sec-title">Giải pháp toàn diện<br/>cho hạng mục GIS</h2>
    <p class="sec-desc">Đội ngũ kỹ sư giàu kinh nghiệm từ các công ty GIS lâu đời, với công nghệ được xây dựng riêng cho quy hoạch Việt Nam.</p>
    <div class="features-grid">
      <div class="feat-card">
        <div class="feat-icon">🔄</div>
        <h3>Chuyển đổi CAD → GIS</h3>
        <p>Chuyển đổi toàn bộ hồ sơ từ định dạng CAD (.dwg, .dxf) sang cơ sở dữ liệu GIS chuẩn GeoPackage theo đúng Thông tư 16.</p>
      </div>
      <div class="feat-card">
        <div class="feat-icon">🔬</div>
        <h3>Quét lỗi tự động</h3>
        <p>Công cụ quét lỗi topology, sai hệ tọa độ, thiếu trường thuộc tính hoàn toàn tự động — đảm bảo sản phẩm đồng nhất với hồ sơ đầu vào.</p>
      </div>
      <div class="feat-card">
        <div class="feat-icon">📦</div>
        <h3>Đóng gói hồ sơ chuẩn</h3>
        <p>Cấu trúc thư mục, đặt tên lớp, trường thuộc tính đúng chuẩn theo quy định — thuận lợi tối đa cho việc thẩm định và nghiệm thu.</p>
      </div>
      <div class="feat-card">
        <div class="feat-icon">🌐</div>
        <h3>Nền tảng WebGIS</h3>
        <p>Hỗ trợ công cụ WebGIS để xem và tra cứu sản phẩm trực tiếp trên web — thuận lợi cho hội đồng thẩm định xem cả bản CAD và GIS song song.</p>
      </div>
      <div class="feat-card">
        <div class="feat-icon">📄</div>
        <h3>Hỗ trợ hồ sơ thầu</h3>
        <p>Sẵn sàng đồng hành hỗ trợ năng lực, hồ sơ dự thầu, hồ sơ nghiệm thu liên quan đến hạng mục GIS từ lần gặp đầu tiên đến nghiệm thu.</p>
      </div>
      <div class="feat-card">
        <div class="feat-icon">🤝</div>
        <h3>Đồng hành toàn gói thầu</h3>
        <p>Từ buổi gặp đầu tiên với chủ đầu tư đến cái bắt tay sau nghiệm thu thành công — chúng tôi ở đây suốt hành trình cùng bạn.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ PROCESS ══════════════════════════════════════════════ -->
<section class="section sec-dark" id="process">
  <div class="container">
    <div class="sec-tag">Quy trình làm việc</div>
    <h2 class="sec-title">Hoàn thành trong 1–3 ngày<br/>với 4 bước đơn giản</h2>
    <div class="process-steps">
      <div class="step">
        <div class="step-num sn1">1</div>
        <h4>Tiếp nhận hồ sơ</h4>
        <p>Bạn gửi hồ sơ CAD + tài liệu quy hoạch. Chúng tôi phân tích và báo giá trong vòng 2 giờ.</p>
      </div>
      <div class="step">
        <div class="step-num sn2">2</div>
        <h4>Chuyển đổi &amp; xử lý</h4>
        <p>Kỹ sư GIS triển khai chuyển đổi, phân lớp đúng mã loại đất, hệ tọa độ VN2000 / EPSG:5897.</p>
      </div>
      <div class="step">
        <div class="step-num sn3">3</div>
        <h4>Quét lỗi &amp; kiểm tra</h4>
        <p>Công cụ tự động quét toàn bộ lỗi topology, thuộc tính, đảm bảo khớp 100% với hồ sơ gốc.</p>
      </div>
      <div class="step">
        <div class="step-num sn4">4</div>
        <h4>Bàn giao &amp; hỗ trợ</h4>
        <p>Giao GeoPackage + WebGIS viewer. Thanh toán sau khi nghiệm thu. Hỗ trợ thẩm định trọn gói.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ COMMITMENTS ═══════════════════════════════════════════ -->
<section class="section" id="commitments">
  <div class="container">
    <div class="sec-tag">Cam kết của chúng tôi</div>
    <h2 class="sec-title">Chúng tôi <span style="color:var(--pl)">cam kết</span> với bạn</h2>
    <div class="commit-grid">
      <div class="commit-item">
        <div class="commit-icon">🤝</div>
        <div>
          <h4>Trách nhiệm cao · Uy tín · Tận tình</h4>
          <p>Đồng hành cùng đối tác với tinh thần trách nhiệm cao nhất. Không bỏ lại đối tác giữa chừng dù gặp bất kỳ khó khăn nào.</p>
        </div>
      </div>
      <div class="commit-item">
        <div class="commit-icon">⚡</div>
        <div>
          <h4>Hoàn thành từ 1–3 ngày làm việc</h4>
          <p>Đảm bảo không để ảnh hưởng đến thời hạn trình thẩm định, trình phê duyệt hồ sơ của đối tác.</p>
        </div>
      </div>
      <div class="commit-item">
        <div class="commit-icon">💰</div>
        <div>
          <h4>Làm trước · Thanh toán sau</h4>
          <p>Chi phí hợp lý và cạnh tranh cao so với thị trường. Thanh toán sau khi nghiệm thu — bạn hoàn toàn không có rủi ro.</p>
        </div>
      </div>
      <div class="commit-item">
        <div class="commit-icon">🔬</div>
        <div>
          <h4>Quét lỗi qua công cụ tự động</h4>
          <p>Đảm bảo kết quả đồng nhất với hồ sơ quy hoạch đầu vào. Không để lọt lỗi topology hay sai thuộc tính.</p>
        </div>
      </div>
      <div class="commit-item">
        <div class="commit-icon">🌐</div>
        <div>
          <h4>WebGIS viewer hỗ trợ thẩm định</h4>
          <p>Công cụ xem và tra cứu sản phẩm trực tiếp trên web — hội đồng thẩm định có thể so sánh CAD và GIS song song mọi lúc.</p>
        </div>
      </div>
      <div class="commit-item">
        <div class="commit-icon">🏆</div>
        <div>
          <h4>Đồng hành từ đầu đến nghiệm thu</h4>
          <p>Từ lần đầu gặp mặt chủ đầu tư cho tới cái bắt tay sau khi nghiệm thu thành công — chúng tôi luôn ở bên bạn.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══ STANDARDS ════════════════════════════════════════════ -->
<section class="section sec-dark" id="standards">
  <div class="container">
    <div class="sec-tag">Tiêu chuẩn kỹ thuật</div>
    <h2 class="sec-title">Tuân thủ đầy đủ<br/>quy định pháp lý</h2>
    <div class="std-wrap">
      <div class="std-list">
        <div class="std-item"><span class="std-badge sb-blue">Thông tư 16</span><p>Lập hồ sơ quy hoạch trên nền GIS song hành từ đầu đến cuối gói thầu</p></div>
        <div class="std-item"><span class="std-badge sb-green">EPSG:5897</span><p>Hệ tọa độ VN2000 chuẩn quốc gia — múi chiếu 3° cho từng tỉnh/thành</p></div>
        <div class="std-item"><span class="std-badge sb-green">VN2000</span><p>Hệ quy chiếu Việt Nam 2000 theo quy định của Bộ Tài nguyên và Môi trường</p></div>
        <div class="std-item"><span class="std-badge sb-purple">GeoPackage</span><p>Định dạng cơ sở dữ liệu GIS chuẩn quốc tế OGC — dễ chia sẻ, không phụ thuộc phần mềm</p></div>
        <div class="std-item"><span class="std-badge sb-blue">TT01/2021</span><p>Quy định kỹ thuật về hệ thống thông tin địa lý phục vụ quy hoạch đô thị</p></div>
      </div>
      <div class="std-visual">
<span class="sv-comment"># Cấu trúc GeoPackage chuẩn TT16</span><br/>
<span class="sv-key">layers</span> = {<br/>
&nbsp;&nbsp;<span class="sv-str">"R_SDD_QH"</span>: {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sv-key">crs</span>: <span class="sv-str">"EPSG:5897"</span>,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sv-key">ma_loai_dat</span>: <span class="sv-str">"ODT"</span>,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sv-key">dien_tich</span>: <span class="sv-num">12453.7</span>,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sv-key">ky_hieu</span>: <span class="sv-str">"Đất ở đô thị"</span>,<br/>
&nbsp;&nbsp;},<br/>
&nbsp;&nbsp;<span class="sv-str">"R_CTXD"</span>: { ... },<br/>
&nbsp;&nbsp;<span class="sv-str">"R_GTCC"</span>: { ... },<br/>
}<br/>
<span class="sv-comment"># ✅ Quét lỗi topology: 0 lỗi</span><br/>
<span class="sv-comment"># ✅ Kiểm tra thuộc tính: OK</span><br/>
<span class="sv-comment"># ✅ Hệ tọa độ: VN2000 / 3°</span>
      </div>
    </div>
  </div>
</section>

<!-- ══ CONTACT ══════════════════════════════════════════════ -->
<section class="cta-section" id="contact">
  <div class="cta-bg"></div>
  <div class="container">
    <div class="contact-card">
      <h2>Bắt đầu ngay hôm nay 🚀</h2>
      <p class="sub">Liên hệ để được tư vấn miễn phí · Làm trước · Thanh toán sau khi nghiệm thu</p>
      <form class="contact-form" onsubmit="handleContact(event)">
        <div class="form-group">
          <label>Họ và tên *</label>
          <input type="text" id="ctName" placeholder="Nguyễn Văn A" required/>
        </div>
        <div class="form-group">
          <label>Số điện thoại *</label>
          <input type="tel" id="ctPhone" placeholder="0901 234 567" required/>
        </div>
        <div class="form-group">
          <label>Email</label>
          <input type="email" id="ctEmail" placeholder="email@congty.vn"/>
        </div>
        <div class="form-group">
          <label>Loại dự án</label>
          <select id="ctType">
            <option value="">-- Chọn loại quy hoạch --</option>
            <option>Quy hoạch sử dụng đất</option>
            <option>Quy hoạch đô thị</option>
            <option>Quy hoạch xây dựng nông thôn</option>
            <option>Quy hoạch giao thông</option>
            <option>Loại khác</option>
          </select>
        </div>
        <div class="form-group full">
          <label>Mô tả yêu cầu</label>
          <textarea id="ctMsg" rows="4" placeholder="Mô tả hồ sơ cần xử lý, diện tích, số lớp... (không bắt buộc)"></textarea>
        </div>
        <div class="form-submit">
          <button type="submit" class="btn btn-green btn-xl">📞 Gửi yêu cầu tư vấn miễn phí</button>
          <p style="margin-top:12px;font-size:13px;color:var(--muted)">Chúng tôi sẽ phản hồi trong vòng 30 phút trong giờ hành chính</p>
        </div>
      </form>
      <div class="contact-direct">
        <div class="cd-item"><span class="cd-icon">📞</span><a href="tel:0332945089" style="color:var(--pl)">0332 945 089</a></div>
        <div class="cd-item"><span class="cd-icon">💬</span><span style="color:var(--muted)">Zalo / Hotline 24/7</span></div>
        <div class="cd-item"><span class="cd-icon">🏢</span><span style="color:var(--muted)">Công ty TNHH Công nghệ Bản đồ GisVN</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ══ FOOTER ═══════════════════════════════════════════════ -->
<footer class="footer">
  <div class="footer-inner">
    <div>
      <div class="footer-logo">🗺 GIS<span style="color:var(--pl)">VN</span></div>
      <p class="footer-desc">Công ty TNHH Công nghệ Bản đồ GisVN — Đối tác GIS chuyên nghiệp cho lập hồ sơ quy hoạch. Tiên phong trong ứng dụng Thông tư 16 tại Việt Nam.</p>
    </div>
    <div>
      <h4>Dịch vụ</h4>
      <div class="footer-links">
        <a href="#features">Chuyển đổi CAD → GIS</a>
        <a href="#features">Quét lỗi tự động</a>
        <a href="#features">WebGIS viewer</a>
        <a href="#features">Hỗ trợ hồ sơ thầu</a>
      </div>
    </div>
    <div>
      <h4>Liên hệ</h4>
      <div class="footer-links">
        <a href="tel:0332945089">📞 0332 945 089</a>
        <a href="#contact">Gửi yêu cầu tư vấn</a>
        <a href="#standards">Tiêu chuẩn kỹ thuật</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2025 Công ty TNHH Công nghệ Bản đồ GisVN</span>
    <span>Tuân thủ Thông tư 16 · EPSG:5897 · GeoPackage</span>
  </div>
</footer>

<script>
// Navbar scroll
window.addEventListener('scroll',()=>{
  document.getElementById('navbar').classList.toggle('scrolled',scrollY>50);
});

// Scroll reveal
const obs = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){e.target.style.opacity='1';e.target.style.transform='translateY(0)';}
  });
},{threshold:.1});
document.querySelectorAll('.feat-card,.commit-item,.pain-card,.step').forEach(el=>{
  el.style.opacity='0';el.style.transform='translateY(24px)';
  el.style.transition='opacity .5s ease,transform .5s ease';
  obs.observe(el);
});

// Contact form
function handleContact(e){
  e.preventDefault();
  const btn=e.target.querySelector('button[type=submit]');
  btn.textContent='✅ Đã gửi! Chúng tôi sẽ liên hệ sớm nhất';
  btn.style.background='linear-gradient(135deg,#10b981,#059669)';
  btn.disabled=true;
  setTimeout(()=>{
    btn.textContent='📞 Gửi yêu cầu tư vấn miễn phí';
    btn.style.background='';
    btn.disabled=false;
  },4000);
}
</script>
</body>
</html>"""

path = os.path.join(BASE, "index.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"✅ Created: {path}")
print("🌐 Open: http://localhost:5501")
