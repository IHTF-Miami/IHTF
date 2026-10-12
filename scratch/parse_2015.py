import re

with open('scratch/teatro/2015 _ teatroavante.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# img tags
img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', html)
print(f"Total img tags: {len(img_tags)}")
for src in img_tags:
    if 'f1540b' in src or '2015' in src or '.jpg' in src or '.png' in src or '.gif' in src or '.jpeg' in src:
        print("IMG:", src)

# richTextElements
pattern = re.compile(r'<div[^>]*data-testid="richTextElement"[^>]*>(.*?)</div>', re.DOTALL)
elements = pattern.findall(html)

with open('scratch/edition_2015_parsed.txt', 'w', encoding='utf-8') as out:
    for idx, el in enumerate(elements):
        text = re.sub(r'<br\s*/?>', '\n', el)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'&nbsp;', ' ', text)
        text = re.sub(r'[ \t]+', ' ', text).strip()
        if text and 'Este sitio web' not in text and 'Wix.com' not in text:
            out.write(f"--- EL {idx} ---\n{text}\n\n")

print("Parsed 2015 text saved to scratch/edition_2015_parsed.txt")
