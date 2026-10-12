import os
import shutil
from PIL import Image

def process_edicion(src_dir, mapping, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    cropped_dir = os.path.join(dest_dir, "cropped")
    os.makedirs(cropped_dir, exist_ok=True)
    
    for i, filename in enumerate(mapping, 1):
        src_path = os.path.join(src_dir, filename)
        assert os.path.exists(src_path), f"File not found: {src_path}"
        
        dest_main = os.path.join(dest_dir, f"{i}.png")
        dest_crop = os.path.join(cropped_dir, f"Obra{i}.png")
        
        im = Image.open(src_path)
        im.save(dest_main, "PNG")
        
        # Crop or resize for thumbnail
        # Let's ensure cropped version has standard 16:10 or 4:3 or original aspect ratio with max bounds
        w, h = im.size
        # Center crop slightly if very tall, or fit
        im.save(dest_crop, "PNG")
        print(f"Processed {i}: {filename} -> {dest_main} ({w}x{h})")

# Mapping 2018 (Edición 33)
dir_2018 = "scratch/teatro/2018 _ teatroavante_files"
map_2018 = [
    "1c8de5_8a72641f71c34a0bbba0e36e4011b5f5~mv2_d_6000_4000_s_4_2.jpg", # 1. Antonio Martorell
    "f1540b_4b8df1d829dc4d108c655eb022bcf3f7~mv2_d_2848_4288_s_4_2.jpg", # 2. Beatriz J. Rizk
    "1c8de5_16da37d473c74d15ba6edacf40c579d9~mv2.jpg",                   # 3. Hij@s de la Bernarda
    "1c8de5_2d2b49f1e7884f70bfa707ed8b7dc218~mv2_d_2448_3264_s_4_2.jpg", # 4. Rosa Luisa Márquez
    "1c8de5_e21629377755465b9752331e3f21e686~mv2_d_3645_2604_s_4_2.jpg", # 5. La última felicidad
    "1c8de5_e18073a232cc46df93bccf8a1c1d1833~mv2.jpg",                   # 6. #malditos16
    "1c8de5_0ac130d78bb54aecb1a7bb672fa706a9~mv2.png",                   # 7. Éramos cuatro
    "1c8de5_6b6ce908b51a4471bc4529916f476e39~mv2_d_4752_2487_s_4_2.jpg", # 8. Unos Dos
    "1c8de5_8a4ca483581d4875936c6b862a27bfbc~mv2_d_2305_1533_s_2.jpg",   # 9. La incapaz
    "1c8de5_c63fa9fb7b3447e484825fc652af1415~mv2.png",                   # 10. El gato y la gaviota (Key Biscayne)
    "1c8de5_0b9e6fb4424a435f8ef6ebaab3b854ba~mv2.png",                   # 11. Día Internacional del Niño (MDCA)
    "0297.jpg",                                                           # 12. En ningún lugar del mundo
    "1c8de5_56fc4bc74a8140639a9a37804bf8e181~mv2_d_3912_3050_s_4_2.jpg"  # 13. Wenses y Lala
]

# Mapping 2019 (Edición 34)
dir_2019 = "scratch/teatro/2019 _ teatroavante_files"
map_2019 = [
    "artista.png",                                                        # 1. Manuel Tricallotis
    "f1540b_4b8df1d829dc4d108c655eb022bcf3f7~mv2_d_2848_4288_s_4_2.jpg", # 2. Beatriz J. Rizk
    "Screen Shot 2019-04-23 at 9_07_05 PM.png",                           # 3. La extinta poética
    "CARTAS DEJENNY 3.jpg",                                               # 4. Cartas de Jenny
    "EL_BULULÚ__ANTOLOGIA_ENDIABLADA.jpg",                                # 5. El Bululú. Antología endiablada
    "BENDITA GLORIA Juan G_ Larrondo   (5) (2.jpg",                       # 6. Bendita gloria
    "Screen Shot 2019-04-24 at 12_31_45 AM_pn.png",                       # 7. Pepe Bable
    "Siete Cabritllos - Teatro Los Claveles 0.jpg",                        # 8. Siete cabritillos (Key Biscayne)
    "Siete Cabritllos - Teatro Los Claveles 0.jpg",                        # 9. Día Internacional del Niño (MDCA)
    "Bayamesa_Familia_2019_JPG.jpg",                                      # 10. Bayamesa
    "MILLONES DE SEGUNDOS (imagen afiche prin.jpg"                         # 11. Millones de segundos
]

print("=== Processing Edición 33 (2018) ===")
process_edicion(dir_2018, map_2018, "assets/Fotos_Archivos/Edicion_33")

print("\n=== Processing Edición 34 (2019) ===")
process_edicion(dir_2019, map_2019, "assets/Fotos_Archivos/Edicion_34")

print("\nALL IMAGES PROCESSED SUCCESSFULLY!")
