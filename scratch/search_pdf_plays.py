import re
import zlib

with open('assets/IHTF_Miami_2026.pdf', 'rb') as f:
    pdf_bytes = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', pdf_bytes, re.DOTALL)

all_chunks = []
for s in streams:
    try:
        decompressed = zlib.decompress(s)
        tj_matches = re.findall(rb'\[(.*?)\]\s*TJ', decompressed)
        for tj in tj_matches:
            parts = re.findall(rb'\((.*?)\)', tj)
            joined = ''.join(p.decode('latin1', errors='ignore') for p in parts)
            if len(joined.strip()) > 1:
                all_chunks.append(joined.strip())
    except:
        pass

with open('scratch/all_pdf_chunks.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(all_chunks))

print(f"Written {len(all_chunks)} chunks to scratch/all_pdf_chunks.txt")

# Let's search for play names in the chunks
play_keywords = ['carrusel', 'zombi', 'jabalí', 'jabali', 'fuego', 'odd man out', 'sueño', 'sueno', 'robinson', 'pundonor', 'hamlet']
for i, line in enumerate(all_chunks):
    for kw in play_keywords:
        if kw in line.lower():
            context = '\n'.join(all_chunks[max(0, i-5):min(len(all_chunks), i+15)])
            print(f"=== Found '{kw}' at line {i}: ===")
            print(context)
            print("-" * 50)
            break
