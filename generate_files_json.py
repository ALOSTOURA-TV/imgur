import os
import json
import subprocess

allowed_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')
files = []

def get_git_date(path):
    try:
        result = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--follow', '--format=%cd', '--date=format:%Y-%m-%d(%p %I:%M:%S)', path],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.stdout.splitlines()[0] if result.stdout else ""
    except:
        return ""

for root, dirs, filenames in os.walk('.'):
    for f in filenames:
        if f.lower().endswith(allowed_exts):
            full_path = os.path.join(root, f)
            if os.path.isfile(full_path):
                rel_path = os.path.relpath(full_path, '.')
                date = get_git_date(rel_path)
                if date:
                    files.append({
                        "name": rel_path,
                        "date": date
                    })

files.sort(key=lambda x: x["date"], reverse=True)

with open('files.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✅ تم تحديث files.json ({len(files)} ملف).")
