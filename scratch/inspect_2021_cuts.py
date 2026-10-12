from PIL import Image

im = Image.open("scratch/teatro/1. Capturas/screencapture-teatroavante-wixsite-teatroavante-2021-2026-10-10-12_51_43.png")
w, h = im.size

# Let's crop vertical sections of the 2021 capture to see each card clearly
# Header is 0..600
# Card 1 (Poster): ~600..1200
# Card 2 (Educativo): ~1200..1700
# Card 3 (Premio): ~1700..2200
# Card 4: ~2200..2800
# Card 5: ~2800..3400
# Card 6: ~3400..4000
# Card 7: ~4000..4600
# Card 8: ~4600..5200
# Card 9 & 10: ~5200..5964

import os
os.makedirs("scratch/cards_2021", exist_ok=True)

cuts = [
    (0, 700, "0_header"),
    (700, 1300, "1_poster"),
    (1300, 1800, "2_educativo"),
    (1800, 2350, "3_premio"),
    (2350, 3050, "4_obra1"),
    (3050, 3750, "5_obra2"),
    (3750, 4350, "6_obra3"),
    (4350, 4950, "7_obra4"),
    (4950, 5550, "8_ninio"),
    (5550, 5964, "9_final")
]

for top, bottom, name in cuts:
    c = im.crop((0, top, w, bottom))
    c.save(f"scratch/cards_2021/{name}.png")
    print(f"Saved {name}: {top}..{bottom}")
