import re

def print_clean(filename):
    print(f"=== {filename} ===")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for l in lines:
        l = l.strip()
        if not l: continue
        # ignore generic navigation items
        if any(nav in l for nav in ['La Compañ', 'Personal', 'Premios', 'PROGRAMA 2025', 'Programa de Mano', 'Calendario', 'Eventos Adicionales', 'Día Internacional', 'Teatros', 'Sponsors', 'ARCHIVOS DEL FESTIVAL', 'CONTACTOS', 'INSCRIPCIONES', 'More', 'Use tab to navigate', 'Este sitio web fue creado', 'Empezar', 'Ir al contenido principal']):
            continue
        print(l)

print_clean("scratch/2018_elements.txt")
