import os
import re
import json

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_teatro = os.path.join(workspace, "scratch", "teatro")

def parse_full_year(year):
    html_path = os.path.join(scratch_teatro, f"{year} _ teatroavante.html")
    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    img_matches = list(re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE))
    
    items = []
    for m in img_matches:
        src = m.group(1)
        if "mv2" in src and "11062b" not in src:
            start_pos = max(0, m.start() - 300)
            end_pos = min(len(html), m.end() + 3000)
            snippet = html[start_pos:end_pos]
            clean_text = re.sub(r'<br\s*/?>', '\n', snippet, flags=re.IGNORECASE)
            clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
            clean_text = re.sub(r'\s+', ' ', clean_text)
            clean_text = clean_text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&#39;', "'")
            items.append({
                "img": src,
                "text": clean_text
            })

    out_file = os.path.join(workspace, "scratch", f"full_{year}_parsed.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"Year {year}: parsed {len(items)} items saved to {out_file}")

parse_full_year(2016)
parse_full_year(2017)
