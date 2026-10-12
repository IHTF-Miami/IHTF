import re

def parse_blocks(html_path, out_path):
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    tag_regex = re.compile(r'(<img[^>]+>|<p[^>]*>.*?<\/p>|<h[1-6][^>]*>.*?<\/h[1-6]>)', re.DOTALL | re.IGNORECASE)
    matches = tag_regex.findall(html)
    
    clean_entries = []
    for m in matches:
        if m.lower().startswith('<img'):
            src_m = re.search(r'src=["\']([^"\']+)["\']', m, re.I)
            alt_m = re.search(r'alt=["\']([^"\']*)["\']', m, re.I)
            src = src_m.group(1) if src_m else ''
            alt = alt_m.group(1) if alt_m else ''
            if any(k in src.lower() for k in ['logo', 'wix', 'banner', 'esp.png', 'usa.png']):
                continue
            clean_entries.append(f"IMAGE: src={src} | alt={alt}")
        else:
            txt = re.sub(r'<[^>]+>', ' ', m)
            txt = ' '.join(txt.split())
            if not txt or len(txt) < 2:
                continue
            if any(k in txt for k in ['Wix', 'JavaScript', 'viewerModel', 'function()', 'var ']):
                continue
            clean_entries.append(f"TEXT: {txt}")

    with open(out_path, 'w', encoding='utf-8') as f:
        for e in clean_entries:
            f.write(e + "\n")
    print(f"Wrote {len(clean_entries)} items to {out_path}")

parse_blocks("scratch/teatro/Program 2022 _ teatroavante.html", "scratch/2022_structured.txt")
parse_blocks("scratch/teatro/2023 _ teatroavante.html", "scratch/2023_structured.txt")
