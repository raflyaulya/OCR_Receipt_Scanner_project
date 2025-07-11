import cv2 
import pytesseract 
import re 
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the Pict 
image = Image.open('receipt11.jpg')

# lis_invoicePict = []
# name_invoicePict = 'invoice'

# for i in range(9):
#     # nameUnited_invoicePict = 'invoice' + str(i +1) + '.jpg'
#     nameUnited_invoicePict = 'invoice_pict/invoice' + str(i +1) + '.jpg'
#     lis_invoicePict.append(nameUnited_invoicePict)
# print(lis_invoicePict)

# image = Image.open(lis_invoicePict)

text = pytesseract.image_to_string(image, lang='rus') 
get_lang = pytesseract.get_languages(config='')


# contoh Parsing 
date = re.search(r'ДАТА:\s*(.+)', text)
amount= re.search(r'Сумма:\s*(.+)', text)
commision= re.search(r'Коммисия:\s*(.+)', text)
# total_price = re.search(r'Итого:\s*(.+)', text)
total_price = re.search(r'ИТОГ\s*(.+)', text)
bik= re.search(r'БИК:\s*(.+)', text)

print()
print("Date:", date.group(1) if date else '-')
print('Amount:', amount.group(1) if amount else '-') 
print('Commision:', commision.group(1) if commision else '-')
print('Total Price:', total_price.group(1) if total_price else '-')
print('БИК:', bik.group(1) if bik else '-')


# Pict Preprocessing 



# OCR + automatic Parsing



# receipt1.png 