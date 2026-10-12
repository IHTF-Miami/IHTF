import os
import re
from PIL import Image

# 1. Check 2021 high-res screenshot
scr_2021 = "scratch/teatro/1. Capturas/screencapture-teatroavante-wixsite-teatroavante-2021-2026-10-10-12_51_43.png"
if os.path.exists(scr_2021):
    im21 = Image.open(scr_2021)
    print(f"2021 capture size: {im21.size}")
else:
    print("2021 capture NOT found!")

# 2. Check 2022 HTML & files
print("\n--- 2022 Files ---")
p22 = "scratch/teatro/Program 2022 _ teatroavante_files"
if os.path.exists(p22):
    f22 = os.listdir(p22)
    img22 = [f for f in f22 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    print(f"2022 images ({len(img22)}):")
    for f in img22:
        print(f"  {f}")

# 3. Check 2023 HTML & files
print("\n--- 2023 Files ---")
p23 = "scratch/teatro/2023 _ teatroavante_files"
if os.path.exists(p23):
    f23 = os.listdir(p23)
    img23 = [f for f in f23 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    print(f"2023 images ({len(img23)}):")
    for f in img23:
        print(f"  {f}")
