import os
import json

allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

# البحث في كل المجلدات الفرعية
files = []
for root, dirs, filenames in os.walk('.'):
    for f in filenames:
        if f.lower().endswith(allowed_exts):
            full_path = os.path.join(root, f)
            # إزالة .\ من البداية للحصول على مسار نسبي
            rel_path = os.path.relpath(full_path, '.')
            files.append(rel_path)

# الترتيب حسب آخر تعديل (الأحدث أولاً)
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم تحديث files.json ({len(files)} ملف).")
