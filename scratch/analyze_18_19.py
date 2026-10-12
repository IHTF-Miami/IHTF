import os
import json
import re
from html.parser import HTMLParser

class WixHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paragraphs = []
        self.images = []
        self.current_tag = None
        self.current_text = []
        self.capture_text = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "img":
            src = attrs_dict.get("src", "")
            alt = attrs_dict.get("alt", "")
            self.images.append({"src": src, "alt": alt, "attrs": attrs_dict})
        if tag in ["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "div"]:
            self.capture_text = True

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.paragraphs.append(text)

def analyze(filename):
    print(f"=== {filename} ===")
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    parser = WixHTMLParser()
    parser.feed(content)
    
    # filter out script/style/wix boilerplates
    clean_p = [p for p in parser.paragraphs if len(p) > 3 and not p.startswith("wix") and not "javascript" in p.lower() and not "{" in p and not "}" in p]
    print(f"Found {len(clean_p)} text blocks")
    for i, p in enumerate(clean_p[:40]):
        print(f"[{i}] {p}")
    
    # Check images referenced in HTML
    img_srcs = set()
    for m in re.finditer(r'src=["\']([^"\']+\.(?:png|jpg|jpeg|gif|avif))["\']', content, re.I):
        img_srcs.add(m.group(1))
    print(f"Found {len(img_srcs)} image sources in HTML:")
    for s in sorted(img_srcs):
        print(f"  {s}")

analyze("scratch/teatro/2018 _ teatroavante.html")
print("\n" + "="*50 + "\n")
analyze("scratch/teatro/2019 _ teatroavante.html")
