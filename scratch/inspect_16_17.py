import os
import re

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_teatro = os.path.join(workspace, "scratch", "teatro")

def inspect_year(year):
    html_path = os.path.join(scratch_teatro, f"{year} _ teatroavante.html")
    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    print(f"\n==================== YEAR {year} ====================")
    img_matches = list(re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE))
    
    count = 0
    play_images = []
    for m in img_matches:
        src = m.group(1)
        if "mv2" in src and "11062b" not in src:
            count += 1
            play_images.append(src)
            # Find snippet around image
            start_pos = max(0, m.start() - 300)
            end_pos = min(len(html), m.end() + 2500)
            snippet = html[start_pos:end_pos]
            clean_text = re.sub(r'<br\s*/?>', '\n', snippet, flags=re.IGNORECASE)
            clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
            clean_text = re.sub(r'\s+', ' ', clean_text)
            clean_text = clean_text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&#39;', "'")
            print(f"\n--- {year} PLAY {count} ---")
            print(f"Img: {src}")
            print(clean_text[:400])

inspect_year(2016)
inspect_year(2017)
