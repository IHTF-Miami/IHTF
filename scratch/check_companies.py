import glob
import re

for html_file in sorted(glob.glob('es/obra-*/index.html')):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    name = html_file.split('\\')[-2] if '\\' in html_file else html_file.split('/')[-2]
    print("=" * 60)
    print("PLAY:", name)
    
    # Check meta description
    m_desc = re.search(r'<meta name="description" content="(.*?)"', content)
    if m_desc:
        print("Meta desc:", m_desc.group(1))
        
    # Check if there is company name anywhere in the file
    for line in content.split('\n'):
        if any(w in line.lower() for w in ['compañía', 'compania', 'teatro avante', 'pitchblack', 'criolla', 'la tirana', 'la belloch']):
            print("Match line:", line.strip()[:120])
