import os
from PIL import Image

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_teatro = os.path.join(workspace, "scratch", "teatro")

dir_2016_files = os.path.join(scratch_teatro, "2016 _ teatroavante_files")
imgs_2016 = [
    "f1540b_2ae8ce88ab464b6f8357ba621c2e1956~mv2_d_1955_2557_s_2.jpg",
    "f1540b_b40dff6f8d7e49e7837522f4d2841d83~mv2_d_3639_2250_s_2.jpg",
    "f1540b_7c74334c597e46bf91089b15c37e4a0f.jpg",
    "f1540b_1fefe999a80a49fb9d0b8cd9c3b0eb46~mv2_d_1641_1425_s_2.jpg",
    "f1540b_4da7d4a6c350427b9932adbfad772e9f~mv1.jpg",
    "f1540b_c25dd7dd74614236909e636cf6d55900~mv2_d_4404_3719_s_4_2.jpg",
    "f1540b_842e79cc2e944b9aa4ea336778761d02~mv2_d_4288_2848_s_4_2.jpg",
    "f1540b_ff06143e51d34ce884bd6c664f671c7d~mv2_d_3402_2973_s_4_2.jpg",
    "f1540b_31d37af2f7764d3bb2df4ef03970165b~mv2_d_3488_2616_s_4_2.jpg",
    "f1540b_16da1fb7ed444b2a884c46fb7bc73418.jpg",
    "f1540b_b9cbd62701004e29b95c40284b39aff2~mv2_d_2848_4288_s_4_2.jpg",
    "f1540b_7983444c3d774a2cb9939e205674cd66~mv2.jpg",
    "f1540b_6eb9f5fd2cf5472181eccd823887a641.jpg"
]

dir_2017_files = os.path.join(scratch_teatro, "2017 _ teatroavante_files")
imgs_2017 = [
    "f1540b_1505468516e14c898e9889796c94116c~mv2_d_2241_1625_s_2.jpg",
    "f1540b_4b8df1d829dc4d108c655eb022bcf3f7~mv2_d_2848_4288_s_4_2.jpg",
    "f1540b_f08a645f4f0042ecb90a665106663084~mv2.jpg",
    "f1540b_45cd5f285ab548fdad374a39886e7b99~mv2_d_3888_2074_s_2.jpg",
    "f1540b_6a15ba7723804f51a0a1519c572846d0~mv2_d_3543_2353_s_2.jpg",
    "f1540b_3f1d0e7fff034f32b64d56ac1ec9ffd2~mv2_d_2992_2000_s_2.jpg",
    "f1540b_fafaf7d08b6a412ebaff83e445d701de~mv2.jpg",
    "f1540b_3f639279afc44e9c951ab1a13fd6cdea~mv2_d_5437_3625_s_4_2.jpg",
    "f1540b_b7b797c727b146cb8456833ae065ceb8~mv2.jpg",
    "f1540b_b95fd37cd45e4add9bc1a1dfe961f8d3~mv2.jpg",
    "1c8de5_57f41eeeb3c24a528aeedfc8d0d282aa~mv2_d_4288_2848_s_4_2.jpg",
    "f1540b_ce4ea9075c5c4219906aef63323c6c19~mv2_d_5184_3456_s_4_2.jpg"
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
            im_rgb = im.convert("RGB")
            w, h = im_rgb.size
            max_edge = max(w, h)
            if max_edge > 800:
                scale = 800 / max_edge
                im_rgb = im_rgb.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
            
            path_i = os.path.join(out_dir, f"{i}.png")
            im_rgb.save(path_i, "PNG", optimize=True)
            
            path_obra = os.path.join(cropped_dir, f"Obra{i}.png")
            im_rgb.save(path_obra, "PNG", optimize=True)
            print(f"Edicion {ed_num} - Obra {i}: saved ({w}x{h} -> {im_rgb.size[0]}x{im_rgb.size[1]})")

print("Processing Edicion 31...")
save_and_crop(dir_2016_files, imgs_2016, 31)

print("\nProcessing Edicion 32...")
save_and_crop(dir_2017_files, imgs_2017, 32)

print("\nDone processing images for 31 and 32!")
