import re
import json

with open('data.js', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Also let's inspect the cards in es/agenda/index.html
with open('es/agenda/index.html', 'r', encoding='utf-8') as f:
    agenda_es = f.read()

with open('en/agenda/index.html', 'r', encoding='utf-8') as f:
    agenda_en = f.read()

print("Read data.js successfully, size:", len(data_content))
print("Read agenda_es successfully, size:", len(agenda_es))
print("Read agenda_en successfully, size:", len(agenda_en))

# Find all play-card-wrapper in es/agenda
wrapper_matches = re.findall(r'<div class="play-card-wrapper ([^"]*)"\s+onclick="window\.location\.href=\'([^\']*)\'"', agenda_es)
print("Found card wrappers in es/agenda:", wrapper_matches)
