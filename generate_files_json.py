import os
import json

# اسم المجلد الحالي
folder = '.'

# الامتدادات المسموح بها
allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

# جمع الملفات فقط التي تطابق الامتدادات
files = [
    f for f in os.listdir(folder)
    if f.lower().endswith(allowed_exts) and os.path.isfile(os.path.join(folder, f))
]

# ترتيب الأسماء
files.sort()

# إنشاء ملف JSON
with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم إنشاء files.json بنجاح ({len(files)} صورة)")
