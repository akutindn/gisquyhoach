import os, re

files = [
    'f:/ARCHILABS_AI/gis-landing/index.html',
    'f:/ARCHILABS_AI/gis-landing/chat_backend.py',
    'f:/ARCHILABS_AI/gis-landing/inject_chat.py'
]

for file_path in files:
    if not os.path.exists(file_path): 
        print(f"Skipping {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Phones
    content = content.replace('0905 131 205', '0332 945 089')
    content = content.replace('0905131205', '0332945089')
    content = content.replace('0905.131.205', '0332.945.089')

    # Step 2: Custom branding fixes
    content = content.replace('<span>GIS<span class="accent">VN</span></span>', '<span>GIS<span class="accent">Quy Hoạch</span></span>')
    content = content.replace('<span>GIS</span><strong>VN</strong>', '<span>GIS</span><strong>Quy Hoạch</strong>')

    # Step 3: Prevent variable mangling
    content = content.replace('GISVN_CHAT_URL', '__TEMP_VAR_URL__')
    content = content.replace('GISVN AI Chat', 'GIS Quy Hoạch AI Chat')
    
    # Step 4: Search and replace the rest
    content = re.sub(r'(?i)\bgisvn\b', 'GIS Quy Hoạch', content)
    
    # Step 5: Put back
    content = content.replace('__TEMP_VAR_URL__', 'GISVN_CHAT_URL')

    # Extra edge cases
    content = content.replace('GIS Quy Hoạch_CHAT', 'GISVN_CHAT')
    content = content.replace('GIS Quy Hoạch_URL', 'GISVN_URL')

    # Facebook fix
    content = content.replace('Facebook GIS Quy Hoạch', 'Facebook GIS Quy Hoạch')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Processed {file_path}')
