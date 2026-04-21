# pip3 install pdfminer.six --break-system-packages

from pdfminer.high_level import extract_text

pdf = "pdf/BOE-A-2010-8067.pdf"
txt = "pdf/BOE-A-2010-8067.txt"

texto = extract_text(pdf)

with open(txt, "w", encoding="utf-8") as f:
    f.write(texto)

print("PDF convertido a TXT")