import json
import os

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"

with open(os.path.join(workspace, "scratch", "full_2016_parsed.json"), "r", encoding="utf-8") as f:
    items_2016 = json.load(f)

print(f"=== 2016 ITEMS ({len(items_2016)}) ===")
for i, item in enumerate(items_2016, 1):
    print(f"\n--- Item {i} ---")
    print(f"Image: {item['img']}")
    # print first 250 chars of text
    print(item['text'][:300])
