from PIL import Image
import os

im = Image.open("scratch/teatro/1. Capturas/screencapture-teatroavante-wixsite-teatroavante-2021-2026-10-10-12_51_43.png")
w, h = im.size
print(f"Full image: {w}x{h}")

# In this 1280px wide capture, let's find the card images on the left side
# Typically x is between 150 and 450
# Let's save slices to inspect
os.makedirs("scratch/slices_2021", exist_ok=True)
slice_h = h // 10
for i in range(10):
    s = im.crop((0, i * slice_h, w, min((i + 1) * slice_h + 100, h)))
    s.save(f"scratch/slices_2021/slice_{i}.png")
print("Saved 10 slices of 2021")
