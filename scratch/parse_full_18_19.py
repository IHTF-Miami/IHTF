import os
import re
import json

def parse_wix_page(html_file, out_file):
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Find viewerModel or text blocks
    # Wix stores page data or text in elements. Let's dump all text containers
    # We can split by section or container or find all text paragraphs with positions
    print(f"Parsing {html_file}...")
    
    # Let's extract all image tags with their IDs/containers and nearby text
    # In Wix, images are in <div id="comp-..." or <wow-image ...> or <img ...>
    from html.parser import HTMLParser

    class CompCollector(HTMLParser):
        def __init__(self):
            super().__init__()
            self.elements = []
            self.current_tag = None
            self.current_id = None
            self.current_text = []

        def handle_starttag(self, tag, attrs):
            attrs_dict = dict(attrs)
            comp_id = attrs_dict.get('id', '')
            src = attrs_dict.get('src', '')
            classes = attrs_dict.get('class', '')
            if tag == 'img':
                self.elements.append(('img', comp_id, src, attrs_dict.get('alt', '')))
            elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']:
                self.current_tag = tag
                self.current_id = comp_id

        def handle_endtag(self, tag):
            if tag == self.current_tag:
                self.current_tag = None

        def handle_data(self, data):
            text = data.strip()
            if text and len(text) > 1:
                self.elements.append(('text', self.current_id, text, self.current_tag))

    parser = CompCollector()
    parser.feed(html)
    
    with open(out_file, 'w', encoding='utf-8') as f:
        for elem in parser.elements:
            f.write(f"{elem}\n")
    print(f"Wrote {len(parser.elements)} elements to {out_file}")

parse_wix_page("scratch/teatro/2018 _ teatroavante.html", "scratch/2018_elements.txt")
parse_wix_page("scratch/teatro/2019 _ teatroavante.html", "scratch/2019_elements.txt")
