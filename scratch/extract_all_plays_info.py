import re
import os
import json

# Let's inspect data.js by reading it and extracting the JS object
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see what keys are in data.js
keys = re.findall(r'"([a-z0-9\-]+)":\s*{', text)
print("Keys in data.js:", keys)

# Also let's inspect the order of plays in es/agenda/index.html
with open('es/agenda/index.html', 'r', encoding='utf-8') as f:
    agenda_es = f.read()

order = re.findall(r'href=\'\.\./obra-([^\'/]+)/\'', agenda_es)
print("Order of plays in agenda:", order)

for k in order:
    # check es/obra-{k}/index.html
    es_path = f'es/obra-{k}/index.html'
    en_path = f'en/obra-{k}/index.html'
    title = ""
    company = ""
    venue = ""
    if os.path.exists(es_path):
        with open(es_path, 'r', encoding='utf-8') as f:
            c = f.read()
            m_title = re.search(r'<title>(.*?)</title>', c)
            m_desc = re.search(r'<meta name="description" content="(.*?)"', c)
            print(f"\n--- {k} ---")
            print(f"ES Title tag: {m_title.group(1) if m_title else ''}")
            print(f"ES Meta desc: {m_desc.group(1) if m_desc else ''}")
