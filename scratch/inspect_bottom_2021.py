from PIL import Image

im = Image.open("scratch/teatro/1. Capturas/screencapture-teatroavante-wixsite-teatroavante-2021-2026-10-10-12_51_43.png")
w, h = im.size

# Let's crop from y = 4500 to h in 400px chunks
for y in range(4000, h, 400):
    c = im.crop((0, y, w, min(y + 450, h)))
    c.save(f"scratch/cards_2021/chunk_{y}.png")
    print(f"Saved chunk_{y}.png")
