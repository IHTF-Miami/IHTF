import re

with open('scratch/all_pdf_chunks.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for the play headline blocks:
# Notice how each play has a section like:
# [PLAY NAME]
# SEPTEMBER ...
# [City, COUNTRY]
# [Company]
# Escrita por / Written by ...
# Dirigida por / Directed by ...
# [VENUE]

# Let's search for "WESTCHESTER", "ARSHT", "KOUBEK", "VILLAGE GREEN" or "KEY BISCAYNE"
venues_keywords = ["WESTCHESTER CULTURAL ARTS CENTER", "CARNIVAL STUDIO THEATER", "KOUBEK CENTER", "KEY BISCAYNE"]

lines = text.split('\n')
for i, l in enumerate(lines):
    for v in venues_keywords:
        if v in l.upper():
            print(f"=== Venue match at line {i}: {l} ===")
            print('\n'.join(lines[max(0, i-25):min(len(lines), i+15)]))
            print("="*60)
