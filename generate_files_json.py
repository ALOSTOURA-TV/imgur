import os
import json

# ابحث في جذر المستودع (مستوى أعلى من مجلد imgur)
folder = '..'

# الامتدادات المسموح بها
allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

# اجمع أسماء الملفات
files = [
    f for f in os.listdir(folder)
    if f.lower().endswith(allowed_exts) and os.path.isfile(os.path.join(folder, f))
]

# رتبها أبجديًا
files.sort()

# احفظها داخل imgur/files.json
with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم إنشاء files.json ({len(files)} صورة)")
