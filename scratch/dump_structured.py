import os
import re

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_teatro = os.path.join(workspace, "scratch", "teatro")

def dump_structured(year):
    html_path = os.path.join(scratch_teatro, f"{year} _ teatroavante.html")
    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    img_matches = list(re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE))
    
    out_lines = []
    out_lines.append(f"==================== YEAR {year} ====================\n")
    
    item_num = 0
    for m in img_matches:
        src = m.group(1)
        if ("f1540b" in src or "1c8de5" in src or "mv2" in src) and not ("11062b" in src or "17f99259" in src):
            item_num += 1
            start = max(0, m.start() - 300)
            end = min(len(html), m.end() + 3500)
            chunk = html[start:end]
            
            clean = re.sub(r'<br\s*/?>', '\n', chunk, flags=re.IGNORECASE)
            clean = re.sub(r'</p>|</div>', '\n', clean, flags=re.IGNORECASE)
            clean = re.sub(r'<[^>]+>', ' ', clean)
            lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in clean.split('\n')]
            lines = [l for l in lines if l]
            
            out_lines.append(f"--- ITEM {item_num} ---")
            out_lines.append(f"IMAGE: {src}")
            out_lines.append("\n".join(lines[:35]))
            out_lines.append("\n" + "="*50 + "\n")

    out_file = os.path.join(workspace, "scratch", f"edition_{year}_full.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print(f"Year {year}: dumped {item_num} items to {out_file}")

dump_structured(2016)
dump_structured(2017)
