import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find src/href that don't start with http/https/data/# etc
pattern = r'(?:src|href)=["\']([^"\']+)["\']'
refs = re.findall(pattern, content)

local_refs = []
for r in refs:
    if not r.startswith(('http', 'https', 'data:', '#', '//', 'mailto:', 'tel:', 'zalo', 'javascript')):
        local_refs.append(r)

unique = sorted(set(local_refs))
print("Local file references:")
for r in unique:
    print(f"  {r}")

if not unique:
    print("  (none - trang chỉ dùng CDN, không cần file local)")
