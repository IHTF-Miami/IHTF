import os
from PIL import Image

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_teatro = os.path.join(workspace, "scratch", "teatro")

# Edicion 29 images
dir_2014_files = os.path.join(scratch_teatro, "2014 _ teatroavante_files")
imgs_2014 = [
    "f1540b_2ef898227808442fa5217cb137274a54~mv2_d_4288_2848_s_4_2.jpg",
    "f1540b_280ae8d4f5bd4f4ebaa225a1c89b4435~mv2_d_2048_1363_s_2.jpg",
    "f1540b_d4689a3471884486bc5616225d948f94~mv2_d_2400_1600_s_2.jpg",
    "f1540b_8aa5a1b489f54678bd13bc03fa46c34f~mv2_d_3888_2592_s_4_2.jpg",
    "f1540b_7fb1f26dae5d46b4a51ef75770d2cbb7~mv2_d_2592_3888_s_4_2.jpg",
    "f1540b_b7f824be077949679ecc967cb8ed057a~mv2_d_2835_1890_s_2.jpg",
    "f1540b_a072380bd56a4de28aa0c902bb5de5d0~mv2_d_3888_2592_s_4_2.jpg",
    "f1540b_f0508b5566fe4119b140545e48941c13~mv2.jpg",
    "f1540b_680146744b9b434daa9689ec0112cb4a~mv2_d_2021_1376_s_2.jpg",
    "f1540b_c816779bf87b4de3a968c6b08b9beba6~mv2_d_2126_1414_s_2.jpg",
    "f1540b_768521be991c4b338282575c51c58330~mv2_d_1471_2125_s_2.jpg",
    "f1540b_8c715b3c92d146dcb895d874e508aef8~mv2.jpeg",
    "f1540b_5d8c5dadd8864f9b9e7bbfcdafc79408~mv2_d_2021_1376_s_2.jpg",
    "f1540b_856dcd55933d43d1b01bd5bd11a362ad~mv2_d_3888_5184_s_4_2.jpg",
    "f1540b_bfad1a9e1e6a49758c62b7ee92cf62e4~mv2_d_3622_2427_s_4_2.jpg",
    "f1540b_bba30a164803438ba143131a569c4a61~mv2_d_1530_2856_s_2.jpg",
    "f1540b_2644191f02b3425ca2312c4d0407e944~mv2_d_1966_1342_s_2.jpg"
]

# Edicion 30 images
dir_2015_files = os.path.join(scratch_teatro, "2015 _ teatroavante_files")
imgs_2015 = [
    "f1540b_c626cdad548e47f1b925dafc98d63fa9~mv2_d_3468_2312_s_2.jpg",
    "f1540b_cc073407b675411ba161daf78d65f770~mv2.jpg",
    "f1540b_413181479cf74382a8eafcae6b733d64~mv2_d_3888_2592_s_4_2.jpg",
    "f1540b_e2699c2d7ed6412e88a15a8791e49f15~mv2_d_4000_2667_s_4_2.jpg",
    "f1540b_6ac22cd031b54e8a9c1cc3413031c0aa~mv2_d_5616_3744_s_4_2.jpg",
    "f1540b_cec70b859d844c6893900fd3d013ef1b~mv2_d_2500_1406_s_2.jpg",
    "f1540b_5e2b35fe1b714a81b6c5e65d92b39739~mv2.jpg",
    "f1540b_1d86b37b0f784158b99c1e1220958452~mv2_d_3008_2000_s_2.jpg",
    "f1540b_1d86b37b0f784158b99c1e1220958452~mv2_d_3008_2000_s_2.jpg",
    "f1540b_c9ad200bbe9c4a0989ab0046a404bcc5~mv2_d_4288_2848_s_4_2.jpg",
    "f1540b_af52d45a36f64572a45b868e0e6c0f6f~mv2_d_4256_2832_s_4_2.jpg",
    "f1540b_b14da0ac459d412eaf247692295e7c14~mv2_d_8000_5858_s_4_2.jpg",
    "f1540b_f34f341457674ddb973c5c774c85a099~mv2.jpg"
]

def save_and_crop(src_dir, img_list, ed_num):
    out_dir = os.path.join(workspace, "assets", "Fotos_Archivos", f"Edicion_{ed_num}")
    cropped_dir = os.path.join(out_dir, "cropped")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(cropped_dir, exist_ok=True)
    
    for i, fname in enumerate(img_list, 1):
        src_path = os.path.join(src_dir, fname)
        if not os.path.exists(src_path):
            print(f"Error: {src_path} does not exist!")
            continue
        
        with Image.open(src_path) as im:
            # Convert RGB if necessary
            im_rgb = im.convert("RGB")
            # If larger than 800px on long edge, resize proportionally
            w, h = im_rgb.size
            max_edge = max(w, h)
            if max_edge > 800:
                scale = 800 / max_edge
                im_rgb = im_rgb.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
            
            # Save {i}.png
            path_i = os.path.join(out_dir, f"{i}.png")
            im_rgb.save(path_i, "PNG", optimize=True)
            
            # Save cropped/Obra{i}.png
            path_obra = os.path.join(cropped_dir, f"Obra{i}.png")
            im_rgb.save(path_obra, "PNG", optimize=True)
            print(f"Edicion {ed_num} - Obra {i}: saved ({w}x{h} -> {im_rgb.size[0]}x{im_rgb.size[1]})")

print("Processing Edicion 29...")
save_and_crop(dir_2014_files, imgs_2014, 29)

print("\nProcessing Edicion 30...")
save_and_crop(dir_2015_files, imgs_2015, 30)

print("\nDone processing images!")
