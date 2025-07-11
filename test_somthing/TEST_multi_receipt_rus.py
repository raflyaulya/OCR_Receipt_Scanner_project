import pytesseract
from PIL import Image
import re
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

# source: Folder berisi receipts
invoice_dir = "invoice_pict"

def parse_invoice_text(text):
    result = {}

    # TOTAL Price
    total_patterns = [r'итого[:\s]*([\d\s,.]+)', 
                      r'total[:\s]*([\d\s,.]+)', 
                      r'amount due[:\s]*([\d\s,.]+)', 
                      r'итог[:\s]*([\d\s,.]+)' ]
    for pat in total_patterns:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            result['Total'] = match.group(1)
            break

    # Date / Time
    date_patterns = [r'дата[:\s]*([\d]{1,2} [а-яА-Я]+ \d{4})', 
                     r'ДАТА[:\s]*([\d]{1,2} [а-яА-Я]+ \d{4})', 
                     r'время[:\s]*([\d]{1,2} [а-яА-Я]+ \d{4})', 
                     r'date[:\s]*([\d/-]+)', 
                     r'(\d{2}[-/]\d{2}[-/]\d{4})']
    for pat in date_patterns:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            result['Date'] = match.group(1)
            break

    # Address
    address_patterns = [r'(ул\..+)', r'(address[:\s].+)', r'(alamat[:\s].+)']
    for pat in address_patterns:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            result['Address'] = match.group(1)
            break

    return result

# Proses semua receipts
for fname in sorted(os.listdir(invoice_dir)):
    if fname.lower().endswith(('.jpg', '.png')):
        print(f"\n========== Parsing {fname} ==========")
        image_path = os.path.join(invoice_dir, fname)
        text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')

        parsed = parse_invoice_text(text)
        for key, val in parsed.items():
            print(f"{key}: {val}")
