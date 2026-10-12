from PIL import Image

im = Image.open("scratch/teatro/1. Capturas/screencapture-teatroavante-wixsite-teatroavante-2021-2026-10-10-12_51_43.png")
w, h = im.size

# Check vertical columns x=250..350 to locate each image
img_rows = []
for y in range(600, h):
    # sample pixels across x=260..320
    is_img = False
    for x in range(250, 350, 10):
        r, g, b, *a = im.getpixel((x, y))
        if r > 30 or g > 30 or b > 30: # not background black
            is_img = True
            break
    img_rows.append((y, is_img))

# Group continuous ranges
ranges = []
in_range = False
start_y = 0
for y, is_img in img_rows:
    if is_img and not in_range:
        in_range = True
        start_y = y
    elif not is_img and in_range:
        in_range = False
        if y - start_y > 40: # filter noise
            ranges.append((start_y, y))
if in_range:
    ranges.append((start_y, h))

print(f"Found {len(ranges)} image regions:")
for i, (sy, ey) in enumerate(ranges, 1):
    print(f"Card {i}: y = {sy}..{ey} (height = {ey - sy})")
    # crop card (both image and text)
    card_crop = im.crop((150, max(0, sy - 40), 1150, min(h, ey + 150)))
    card_crop.save(f"scratch/cards_2021/full_card_{i}.png")
