import os
import json

# ابحث في جذر المستودع بدل مجلد imgur
folder = '..'  # ←⬅️ صعد مستوى واحد من مجلد imgur

allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

files = [
    f for f in os.listdir(folder)
    if f.lower().endswith(allowed_exts) and os.path.isfile(os.path.join(folder, f))
]

files.sort()

# احفظ الناتج داخل مجلد imgur
with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم إنشاء files.json بنجاح ({len(files)} صورة)")
