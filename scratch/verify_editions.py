import os
import re

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"

pages = [
    os.path.join(workspace, "es", "archivos-del-festival", "2014", "index.html"),
    os.path.join(workspace, "en", "archivos-del-festival", "2014", "index.html"),
    os.path.join(workspace, "es", "archivos-del-festival", "2015", "index.html"),
    os.path.join(workspace, "en", "archivos-del-festival", "2015", "index.html")
]

all_ok = True

for page in pages:
    if not os.path.exists(page):
        print(f"FAILED: {page} does not exist!")
        all_ok = False
        continue
    
    with open(page, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check img src
    img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"\nChecking {os.path.relpath(page, workspace)}: {len(img_matches)} images")
    
    page_dir = os.path.dirname(page)
    for src in img_matches:
        if src.startswith("http"):
            continue
        # resolve relative path
        resolved = os.path.normpath(os.path.join(page_dir, src.replace("%20", " ")))
        if not os.path.exists(resolved):
            print(f"  MISSING IMG: {src} -> {resolved}")
            all_ok = False
        else:
            # pass
            pass

    # Check css links
    css_matches = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
    for href in css_matches:
        clean_href = href.split("?")[0]
        resolved = os.path.normpath(os.path.join(page_dir, clean_href.replace("%20", " ")))
        if not os.path.exists(resolved):
            print(f"  MISSING CSS: {href} -> {resolved}")
            all_ok = False

if all_ok:
    print("\nALL CHECKS PASSED PERFECTLY!")
else:
    print("\nSOME CHECKS FAILED!")
