import os
import json
from datetime import datetime

allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

files = []
for root, dirs, filenames in os.walk('.'):
    for f in filenames:
        if f.lower().endswith(allowed_exts):
            full_path = os.path.join(root, f)
            if os.path.isfile(full_path):
                rel_path = os.path.relpath(full_path, '.')
                mtime = os.path.getmtime(full_path)
                files.append({
                    "name": rel_path,
                    "date": datetime.fromtimestamp(mtime).isoformat()
                })

# الترتيب من الأحدث إلى الأقدم
files.sort(key=lambda x: x["date"], reverse=True)

with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم تحديث files.json ({len(files)} ملف).")
