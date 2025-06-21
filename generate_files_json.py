import os
import json

folder = '.'
allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

# الحصول على الملفات وتواريخ التعديل
files = [
    f for f in os.listdir(folder)
    if f.lower().endswith(allowed_exts)
    and os.path.isfile(os.path.join(folder, f))
    and not f.startswith('.')
]

# الترتيب من الأحدث إلى الأقدم باستخدام التاريخ 
files.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)), reverse=True)

# حفظها في JSON
with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم تحديث files.json ({len(files)} ملف - مرتب من الأحدث للأقدم).")

