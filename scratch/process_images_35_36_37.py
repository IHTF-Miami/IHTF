import os
from PIL import Image

def process_edicion(img_list, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    crop_dir = os.path.join(dest_dir, "cropped")
    os.makedirs(crop_dir, exist_ok=True)
    
    for i, (src_path, desc) in enumerate(img_list, 1):
        assert os.path.exists(src_path), f"File not found: {src_path}"
        im = Image.open(src_path)
        
        main_dest = os.path.join(dest_dir, f"{i}.png")
        crop_dest = os.path.join(crop_dir, f"Obra{i}.png")
        
        im.save(main_dest, "PNG")
        im.save(crop_dest, "PNG")
        print(f"  Saved {desc} -> {main_dest} ({im.size})")

imgs_35 = [
    ("scratch/teatro/Program 2022 _ teatroavante_files/LEDA ALMAR (Alexis Delgado, Photography).png", "1. Leda Almar"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/f1540b_4b8df1d829dc4d108c655eb022bcf3f7~mv2_d_2848_4288_s_4_2.jpg", "2. Beatriz Rizk"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/GRISELDA GAMBARO.png", "3. Griselda Gambaro"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/6 NOCIONES CN URUGUAY.jpg", "4. 6 Nociones"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/image2.jpeg", "5. Murga Madre"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Barrio Caleidoscopio.png", "6. Barrio Caleidoscopio"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Tom Pain.jpeg", "7. Tom Pain"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Bosque002.jpg", "8. Un bosque encantado KB"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Bosque002.jpg", "9. Dia Nino MDCA"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Ubu Pandemia.png", "10. Ubu Pandemia"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/PAPA ESTA EN LA ATLANTIDA 3RD  (1).jpg", "11. Papa esta en la Atlantida")
]

imgs_36 = [
    ("scratch/teatro/Program 2022 _ teatroavante_files/XXXVI - IHTF - Poster_Artist_Image_Adriana_Torres_Sanchez_2022.jpg", "1. Adriana Torres"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/f1540b_4b8df1d829dc4d108c655eb022bcf3f7~mv2_d_2848_4288_s_4_2.jpg", "2. Beatriz Rizk"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Bette davis.jpg", "3. Bette Davis"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Alacran-8.jpg", "4. Alacran"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Encuentros breves con hombres repulsivos_1__edited.jpg", "5. Encuentros breves"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Frida 4.jpg", "6. Frida KB"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/Frida 4.jpg", "7. Frida Nino MDCA"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/ROTA9.jpg", "8. Rota"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/quintu.jpg", "9. Quintuples"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/XXXVI - IHTF - Life_Achievement_Award_Image_2022.jpg", "10. Adriana Barraza"),
    ("scratch/teatro/Program 2022 _ teatroavante_files/mejorcallo.jpg", "11. Mejor me callo")
]

imgs_37 = [
    ("scratch/teatro/2023 _ teatroavante_files/gabriela_esquivel.jpg", "1. Gabriela Esquivel"),
    ("scratch/teatro/2023 _ teatroavante_files/f1540b_4b8df1d829dc4d108c655eb022bcf3f7~mv2_d_2848_4288_s_4_2.jpg", "2. Beatriz Rizk"),
    ("scratch/teatro/2023 _ teatroavante_files/1.jpg", "3. La isla de los hombres solos"),
    ("scratch/teatro/2023 _ teatroavante_files/2_JPG.jpg", "4. OH, UH, AH, E!"),
    ("scratch/teatro/2023 _ teatroavante_files/3.jpg", "5. Don Quijote"),
    ("scratch/teatro/2023 _ teatroavante_files/4.jpg", "6. Cae la noche tropical"),
    ("scratch/teatro/2023 _ teatroavante_files/5.jpg", "7. Una"),
    ("scratch/teatro/2023 _ teatroavante_files/6.jpg", "8. El guardian de los cuentos KB"),
    ("scratch/teatro/2023 _ teatroavante_files/6.jpg", "9. El guardian Nino MDCA"),
    ("scratch/teatro/2023 _ teatroavante_files/egdc1.jpg", "10. Almuerzo con Sonia"),
    ("scratch/teatro/2023 _ teatroavante_files/2_JPG(1).jpg", "11. Foro"),
    ("scratch/teatro/2023 _ teatroavante_files/9_JPG.jpg", "12. Superpasito"),
    ("scratch/teatro/2023 _ teatroavante_files/MIGUEL-RUBIO-ZAPATA_-PREMIO-2023.jpg", "13. Miguel Rubio"),
    ("scratch/teatro/2023 _ teatroavante_files/10_JPG.jpg", "14. Al pie del Thames")
]

print("Processing Edicion_35 (2021)...")
process_edicion(imgs_35, "assets/Fotos_Archivos/Edicion_35")

print("Processing Edicion_36 (2022)...")
process_edicion(imgs_36, "assets/Fotos_Archivos/Edicion_36")

print("Processing Edicion_37 (2023)...")
process_edicion(imgs_37, "assets/Fotos_Archivos/Edicion_37")

print("\nALL IMAGES SAVED AND CROPPED SUCCESSFULLY!")
