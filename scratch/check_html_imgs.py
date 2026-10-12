import re

def check_html_images(html_file):
    print(f"=== Images referenced in {html_file} ===")
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    matches = re.findall(r'src=["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']', content, re.I)
    unique_matches = set(matches)
    for m in sorted(unique_matches):
        print(f"  {m}")

check_html_images("scratch/teatro/Program 2022 _ teatroavante.html")
print("\n" + "="*50 + "\n")
check_html_images("scratch/teatro/2023 _ teatroavante.html")
