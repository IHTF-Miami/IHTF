import os
import re
import json

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_teatro = os.path.join(workspace, "scratch", "teatro")

def dump_all_elements(year):
    html_path = os.path.join(scratch_teatro, f"{year} _ teatroavante.html")
    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Find all images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"=== ALL IMAGES IN {year} ({len(imgs)}) ===")
    for i, img in enumerate(imgs):
        print(f"  {i}: {img}")

    # Find all text blocks (e.g. data-testid="rich-text-container" or <p>)
    text_blocks = re.findall(r'<div[^>]+data-testid=["\']rich-text-container["\'][^>]*>(.*?)</div>', html, re.DOTALL)
    if not text_blocks:
        text_blocks = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
    
    clean_blocks = []
    for b in text_blocks:
        b_clean = re.sub(r'<br\s*/?>', '\n', b, flags=re.IGNORECASE)
        b_clean = re.sub(r'<[^>]+>', ' ', b_clean)
        b_clean = re.sub(r'\s+', ' ', b_clean)
        b_clean = b_clean.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&#39;', "'").strip()
        if b_clean and len(b_clean) > 5:
            clean_blocks.append(b_clean)
            
    print(f"\n=== CLEAN TEXT BLOCKS IN {year} ({len(clean_blocks)}) ===")
    with open(os.path.join(workspace, "scratch", f"{year}_blocks.txt"), "w", encoding="utf-8") as out:
        for i, b in enumerate(clean_blocks):
            out.write(f"--- BLOCK {i} ---\n{b}\n\n")

dump_all_elements(2016)
dump_all_elements(2017)
