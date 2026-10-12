import os
from PIL import Image

output_dir = 'assets/Fotos_Archivos/Edicion_40'
cropped_dir = os.path.join(output_dir, 'cropped')
os.makedirs(cropped_dir, exist_ok=True)

# Play source images:
# 1. Carrusel: 'assets/f9bb5bfefcbf580338da65d3b9a672234de1553f.png' (or 'assets/40thIHTF - FOTOS de OBRAS/obra-carrusel/Carrusel-HiRes_Jun26-008.webp')
# 2. Zombi Manifiesto: 'assets/40thIHTF - FOTOS de OBRAS/obra-zombi-manifiesto/Copia de ZOMBI FOTO 1.webp'
# 3. Historia de un jabalí: 'assets/40thIHTF - FOTOS de OBRAS/obra-historia-de-un-jabali/Copia de JABALI FOTO 2.webp' (or 'assets/07fb4fbd9864c0979b71bc86cf6ea90268b59cc0.png')
# 4. A fuego: 'assets/40thIHTF - FOTOS de OBRAS/obra-a-fuego/A FUEGO FOTO 1.webp'
# 5. Odd Man Out: 'assets/40thIHTF - FOTOS de OBRAS/obra-odd-man-out/OMO FOTO 1.webp'
# 6. Sueño: 'assets/40thIHTF - FOTOS de OBRAS/obra-sueno/Copia de SUENO FOTO 1.webp'
# 7. Pundonor: 'assets/40thIHTF - FOTOS de OBRAS/obra-pundonor/PUNDONOR FOTO 1.webp'
# 8. Robinson Crusoe: 'assets/40thIHTF - FOTOS de OBRAS/obra-robinson-crusoe/Copia de ROBINSON FOTO 1.webp'
# 9. Hamlet: 'assets/40thIHTF - FOTOS de OBRAS/obra-hamlet/Copia de HAMLET FOTO 1.webp'

sources = [
    (1, 'assets/40thIHTF - FOTOS de OBRAS/obra-carrusel/Carrusel-HiRes_Jun26-008.webp'),
    (2, 'assets/40thIHTF - FOTOS de OBRAS/obra-zombi-manifiesto/Copia de ZOMBI FOTO 1.webp'),
    (3, 'assets/07fb4fbd9864c0979b71bc86cf6ea90268b59cc0.png'),
    (4, 'assets/40thIHTF - FOTOS de OBRAS/obra-a-fuego/A FUEGO FOTO 1.webp'),
    (5, 'assets/40thIHTF - FOTOS de OBRAS/obra-odd-man-out/OMO FOTO 1.webp'),
    (6, 'assets/40thIHTF - FOTOS de OBRAS/obra-sueno/Copia de SUENO FOTO 1.webp'),
    (7, 'assets/40thIHTF - FOTOS de OBRAS/obra-pundonor/PUNDONOR FOTO 1.webp'),
    (8, 'assets/40thIHTF - FOTOS de OBRAS/obra-robinson-crusoe/Copia de ROBINSON FOTO 1.webp'),
    (9, 'assets/40thIHTF - FOTOS de OBRAS/obra-hamlet/Copia de HAMLET FOTO 1.webp')
]

TARGET_WIDTH = 398
TARGET_HEIGHT = 266
TARGET_RATIO = TARGET_WIDTH / TARGET_HEIGHT

for num, src in sources:
    if not os.path.exists(src):
        print(f"Error: {src} does not exist!")
        continue
    
    im = Image.open(src).convert('RGB')
    w, h = im.size
    current_ratio = w / h
    
    if current_ratio > TARGET_RATIO:
        # Image is wider than target ratio: crop width
        new_w = int(h * TARGET_RATIO)
        offset = (w - new_w) // 2
        im_cropped = im.crop((offset, 0, offset + new_w, h))
    else:
        # Image is taller than target ratio: crop height
        new_h = int(w / TARGET_RATIO)
        offset = (h - new_h) // 2
        im_cropped = im.crop((0, offset, w, offset + new_h))
    
    im_resized = im_cropped.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
    
    out_path_num = os.path.join(output_dir, f"{num}.png")
    out_path_obra = os.path.join(cropped_dir, f"Obra{num}.png")
    
    im_resized.save(out_path_num, format="PNG", optimize=True)
    im_resized.save(out_path_obra, format="PNG", optimize=True)
    print(f"Processed Obra {num}: saved to {out_path_num} and {out_path_obra} ({TARGET_WIDTH}x{TARGET_HEIGHT})")

print("All Edition 40 images processed successfully!")
