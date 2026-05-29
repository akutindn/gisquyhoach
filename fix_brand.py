import re

path = r'f:\ARCHILABS_AI\gis-landing\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

replacements = [
    # Phone numbers - all formats
    ('0905 131 205', '0332 945 089'),
    ('0905131205', '0332945089'),
    
    # Title/meta tags
    ('GisVN —', 'GIS Quy Hoạch —'),
    ('GisVN |', 'GIS Quy Hoạch |'),
    
    # Nav logo text
    ('<span>GIS</span><strong>VN</strong>', '<span>GIS</span><strong>Quy Hoạch</strong>'),
    
    # Footer company visible text
    ('Công ty TNHH Công nghệ Bản đồ GisVN', 'GIS Quy Hoạch'),
    ('Facebook GisVN', 'Facebook GIS Quy Hoạch'),
    ('© 2025 Công ty TNHH Công nghệ Bản đồ GisVN', '© 2025 GIS Quy Hoạch'),
    
    # Before/after section
    ('khi có GisVN', 'khi có GIS Quy Hoạch'),
    
    # Testimonial
    ('gặp GisVN. Hợp đồng tiếp theo, GisVN', 'gặp GIS Quy Hoạch. Hợp đồng tiếp theo, GIS Quy Hoạch'),
    
    # FAQ mentions
    ('GisVN có thể tham gia', 'GIS Quy Hoạch có thể tham gia'),
    ('của GisVN. Chúng tôi đồng hành', 'của GIS Quy Hoạch. Chúng tôi đồng hành'),
    ('cam kết cốt lõi của GisVN', 'cam kết cốt lõi của GIS Quy Hoạch'),
    
    # AI widget
    ('trợ lý AI của GisVN', 'trợ lý AI của GIS Quy Hoạch'),
    
    # Contact cd-item
    ('Công ty TNHH Công nghệ Bản đồ GisVN', 'GIS Quy Hoạch'),
    
    # Zalo fallback message phone (escaped in JS)
    ("zalo.me/0905131205", "zalo.me/0332945089"),
    
    # tel: links
    ('href="tel:0905131205"', 'href="tel:0332945089"'),
]

count_total = 0
for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f'  [{count}x] "{old[:55]}" -> "{new[:55]}"')
        count_total += count

print(f'\nTotal replacements: {count_total}')
print(f'Size: {original_len} -> {len(content)} chars')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Saved successfully!')
