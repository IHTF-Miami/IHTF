import os
import re

files_to_check = [
    ('es/archivos-del-festival/2026/index.html', 'es'),
    ('en/archivos-del-festival/2026/index.html', 'en'),
    ('es/archivos-del-festival/index.html', 'grid_es'),
    ('en/archivos-del-festival/index.html', 'grid_en')
]

for rel_path, kind in files_to_check:
    print(f"\n--- Checking {rel_path} ---")
    if not os.path.exists(rel_path):
        print("ERROR: File missing!")
        continue
    with open(rel_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'grid' in kind:
        # Check card 40
        m = re.search(r'<a href="2026/" class="edition-card"><img src="../../assets/archivos-del-festival/40\.avif"[^>]*></a>', content)
        if m:
            print("OK: Card 40 is correctly linked to 2026/:", m.group(0))
        else:
            print("FAIL: Card 40 link not found!")
    else:
        # Check title, plays count, images exist
        m_title = re.search(r'<title>(.*?)</title>', content)
        print("Title:", m_title.group(1) if m_title else "NONE")
        
        plays = re.findall(r'<article class="play-item">', content)
        print(f"Total plays: {len(plays)} (expected 9)")
        
        # Check image paths
        img_srcs = re.findall(r'<div class="play-thumb">\s*<img src="(.*?)"', content)
        print(f"Total play images: {len(img_srcs)}")
        for src in img_srcs:
            # resolve relative to file location
            file_dir = os.path.dirname(rel_path)
            resolved = os.path.normpath(os.path.join(file_dir, src))
            if os.path.exists(resolved):
                print(f"  OK: Image exists -> {src} ({os.path.getsize(resolved)} bytes)")
            else:
                print(f"  FAIL: Image missing -> {resolved}")
        
        # Check footer newsletter
        if 'data-form-id="6b84846d-b4c9-4b02-867d-09c8a7ac5d40"' in content:
            print("OK: Newsletter Constant Contact form present")
        else:
            print("FAIL: Newsletter form missing")
            
        if '_ctct_m = "a79e89c0998befa80793c5464469c842"' in content:
            print("OK: Constant Contact script present")
        else:
            print("FAIL: Constant Contact script missing")
            
        # Check logos
        if 'logo%20blanco.png' in content and 'logo%20colores.png' in content:
            print("OK: Header logos present")
        else:
            print("FAIL: Header logos missing")

print("\nVerification script finished.")
