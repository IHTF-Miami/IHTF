import re
import zlib

with open('assets/IHTF_Miami_2026.pdf', 'rb') as f:
    pdf_bytes = f.read()

streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', pdf_bytes, re.DOTALL)
print(f"Total streams: {len(streams)}")

all_chunks = []
for s in streams:
    try:
        decompressed = zlib.decompress(s)
        # Look for [ ... ] TJ
        tj_matches = re.findall(rb'\[(.*?)\]\s*TJ', decompressed)
        for tj in tj_matches:
            # extract string parts in parentheses
            parts = re.findall(rb'\((.*?)\)', tj)
            joined = ''.join(p.decode('latin1', errors='ignore') for p in parts)
            if len(joined.strip()) > 3:
                all_chunks.append(joined.strip())
    except:
        pass

print(f"Extracted {len(all_chunks)} TJ chunks.")
for c in all_chunks[:30]:
    print(c)
