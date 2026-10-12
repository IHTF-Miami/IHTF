import os
import re
from html.parser import HTMLParser

class ValidatorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.css_links = []
        self.play_count = 0
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "img":
            src = attrs_dict.get("src")
            if src:
                self.images.append(src)
        elif tag == "link":
            if attrs_dict.get("rel") == "stylesheet":
                href = attrs_dict.get("href")
                if href:
                    self.css_links.append(href)
        elif tag == "article":
            classes = attrs_dict.get("class", "").split()
            if "play-item" in classes:
                self.play_count += 1

def validate_page(html_path, expected_plays):
    print(f"Checking {html_path}...")
    assert os.path.exists(html_path), f"File does not exist: {html_path}"
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    parser = ValidatorParser()
    parser.feed(html)
    dir_path = os.path.dirname(html_path)
    
    # Check images
    for src in parser.images:
        if src.startswith("http"):
            continue
        src_clean = src.split("?")[0].replace("%20", " ")
        full_path = os.path.normpath(os.path.join(dir_path, src_clean))
        assert os.path.exists(full_path), f"Missing image: {src} -> {full_path} in {html_path}"
    print(f"  All {len(parser.images)} images valid.")
    
    # Check css
    for href in parser.css_links:
        if href.startswith("http"):
            continue
        href_clean = href.split("?")[0].replace("%20", " ")
        full_path = os.path.normpath(os.path.join(dir_path, href_clean))
        assert os.path.exists(full_path), f"Missing CSS: {href} -> {full_path} in {html_path}"
    print(f"  All {len(parser.css_links)} CSS links valid.")
    
    # Check plays count
    assert parser.play_count == expected_plays, f"Expected {expected_plays} plays, found {parser.play_count} in {html_path}"
    print(f"  Play count matches: {parser.play_count}.")

validate_page("es/archivos-del-festival/2016/index.html", 13)
validate_page("en/archivos-del-festival/2016/index.html", 13)
validate_page("es/archivos-del-festival/2017/index.html", 12)
validate_page("en/archivos-del-festival/2017/index.html", 12)

# Check main index grids
for p in ["es/archivos-del-festival/index.html", "en/archivos-del-festival/index.html"]:
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    assert 'href="2016/"' in c, f"Missing 2016 link in {p}"
    assert 'href="2017/"' in c, f"Missing 2017 link in {p}"
    print(f"  {p} successfully links to 2016/ and 2017/.")

print("\n>>> ALL CHECKS PASSED PERFECTLY! <<<")
