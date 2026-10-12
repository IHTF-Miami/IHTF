import re
import zlib

with open('assets/IHTF_Miami_2026.pdf', 'rb') as f:
    pdf_bytes = f.read()

# Find all streams
streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', pdf_bytes, re.DOTALL)
print(f"Total streams: {len(streams)}")

all_text = []
for s in streams:
    try:
        decompressed = zlib.decompress(s)
        # Look for text operators like (text) Tj or [(text)] TJ
        # or simple text
        txt_matches = re.findall(rb'\((.*?)\)\s*Tj', decompressed)
        for t in txt_matches:
            try:
                dec = t.decode('utf-8', errors='ignore')
                if len(dec.strip()) > 1:
                    all_text.append(dec.strip())
            except:
                pass
    except:
        pass

print(f"Extracted {len(all_text)} text fragments.")
with open('scratch/pdf_text.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(all_text))

print("Saved to scratch/pdf_text.txt. Let's see some samples:")
for t in all_text[:30]:
    print(t)
