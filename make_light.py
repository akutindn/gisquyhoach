import sys

def go():
    file_path = 'f:/ARCHILABS_AI/gis-landing/index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading: {e}")
        return

    # Replace Da Nang mentions
    content = content.replace('DaNang', 'ToanQuoc')
    content = content.replace('Đà Nẵng', 'Toàn Quốc')
    content = content.replace('EPSG:5897', 'VN2000')
    content = content.replace('EPSG 5897', 'VN2000')

    # Add light theme CSS override
    overrides = """
/* ── LIGHT THEME OVERRIDES ── */
:root {
  --bg: #ffffff;
  --bg2: #f8fafc;
  --surface: #ffffff;
  --glass: rgba(255,255,255,0.85);
  --border: rgba(0,0,0,0.08);
  --text: #0f172a;
  --muted: #475569;
  --dim: #94a3b8;
  --primary: #2563eb;
  --pl: #3b82f6;
  --shadow: 0 12px 32px rgba(0,0,0,0.06);
}

body { background: var(--bg); color: var(--text); }
.navbar { background: rgba(255,255,255,0.9); }
.nav-mobile-menu { background: rgba(255,255,255,0.98); }
.nav-hamburger span { background: var(--text); }

.hero-bg { background: linear-gradient(160deg, #f1f5f9 0%, #ffffff 60%, #e0e7ff 100%); }
.hero-grid { background-image: linear-gradient(rgba(37,99,235,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(37,99,235,0.05) 1px, transparent 1px); }

.gis-card { background: #ffffff; box-shadow: 0 24px 60px rgba(0,0,0,0.1); border-color: rgba(0,0,0,0.1); }
.gis-topbar { background: #f8fafc; border-bottom: 1px solid var(--border); }
.gis-title-bar { color: #64748b; }
.gis-map-wrap { background: #f1f5f9; border-bottom: 1px solid var(--border); }
.gis-graticule { background-image: linear-gradient(rgba(0,0,0,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.04) 1px, transparent 1px); }
.gis-coord-label { color: #94a3b8; }
.map-poly-label { background: rgba(255,255,255,0.85); color: #0f172a; }
.map-north { color: #475569; }
.scale-bar { background: linear-gradient(90deg, #0f172a 50%, #3b82f6 50%); border-color: rgba(0,0,0,0.1); }
.scale-lbl { color: #475569; }
.gis-sw-bar { background: rgba(255,255,255,0.9); border-top: 1px solid var(--border); }

.gis-attr-table { background: #ffffff; border-top: 1px solid var(--border); }
.attr-table th { background: #f8fafc; color: #475569; border-bottom: 1px solid var(--border); }
.attr-table td { border-bottom: 1px solid var(--border); }
.td-fid, .td-num { color: #2563eb; }
.td-str { color: #10b981; }
.attr-table tr.sel-row { background: rgba(37,99,235,0.1); }
.attr-table tr:hover { background: rgba(0,0,0,0.02); }

.gis-layers-panel { background: #ffffff; }
.layer-row { background: #f8fafc; }
.layer-name { color: #334155; }
.gis-progress-bar { background: #e2e8f0; }

.floating-badge { background: rgba(255,255,255,0.95); border: 1px solid var(--border); color: #0f172a; box-shadow: 0 8px 24px rgba(0,0,0,0.08); }

.sec-dark { background: #f8fafc; }
.trust-bar { background: #f8fafc; }

.pain-card::before { background: linear-gradient(135deg, rgba(239,68,68,0.02), transparent); }
.pain-quote { background: #f8fafc; border-color: var(--border); }
.pain-quote blockquote { color: #1e293b; }

.feat-card { background: #ffffff; }

.step-num { background: #ffffff; }

.commit-item { background: #ffffff; }

.std-item { background: #ffffff; }
.std-visual { background: #f1f5f9; border-color: var(--border); }

.contact-card { background: rgba(255,255,255,0.95); border-color: var(--border); }
.form-group input, .form-group textarea, .form-group select { background: #f8fafc; border: 1.5px solid var(--border); color: var(--text); }
.form-group input:focus, .form-group textarea:focus, .form-group select:focus { background: #ffffff; }
.form-group select option { background: #ffffff; }

.case-card { background: #ffffff; }
.case-problem { background: rgba(239,68,68,0.04); }
.case-solution { background: rgba(16,185,129,0.04); }

.testi-card { background: #ffffff; }
.testi-card blockquote { color: #334155; }
.testi-card.featured { background: #f8fafc; border-color: rgba(37,99,235,0.2); }

.ba-col { background: #ffffff; }
.ba-col.after { background: #f0fdf4; }
.ba-col.before { background: #fef2f2; }
.ba-list li { color: #475569; }

.price-card { background: #ffffff; }
.price-card.featured { background: #f8fafc; border-color: var(--primary); }

.faq-item { background: #ffffff; }
.faq-q { color: #1e293b; }

.footer { background: #f8fafc; }

.ai-chat-panel { background: #ffffff; }
.acp-header { background: #f8fafc; }
.acp-msgs { background: #f1f5f9; }
.chat-msg.bot .msg-bubble { background: #ffffff; color: #1e293b; border-color: var(--border); }
.typing-dots { background: #ffffff; border-color: var(--border); }
.acp-input { background: #ffffff; color: var(--text); border-color: var(--border); }
.acp-quick { border-top-color: var(--border); }
.acp-info strong { color: #0f172a; }
"""

    if "/* ── LIGHT THEME OVERRIDES ── */" not in content:
        # insert right before </style>
        content = content.replace('</style>', overrides + '\n</style>')

    # specific map label colors fix which might be hardcoded in HTML style="..."
    # like rgba(160,195,255,.7) inside html? We can safely leave it if it looks ok, 
    # but the above CSS overrides should cover most UI.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")

if __name__ == '__main__':
    go()
