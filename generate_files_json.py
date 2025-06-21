import os
import json

allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

files = [
    f for f in os.listdir('.')
    if f.lower().endswith(allowed_exts) and os.path.isfile(f)
]

files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم تحديث files.json ({len(files)} ملف).")
