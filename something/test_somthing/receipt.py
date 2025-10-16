import cv2 
import pytesseract 
import numpy as np
import re 
from PIL import Image

# ==============        STEP 1: PREPROCESSING   =====================
img = cv2.imread('receipt11.jpg')

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding
_, thresh= cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Noise Removal 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
opening= cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) 

# # save hasil
# cv2.imwrite('preprocessed_receipt.png', opening) 

# ==============        STEP 2: OCR + REGEX PARSING    =====================
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# image = Image.open('preprocessed_receipt.png')
# img = cv2.imread('receipt1.jpg')
# image = Image.open('receipt1.jpg')
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
image = img
text = pytesseract.image_to_string(image, lang='rus') 
get_lang = pytesseract.get_languages(config='')


# contoh Parsing 
date = re.search(r'ДАТА:\s*(.+)', text)
amount= re.search(r'Сумма:\s*(.+)', text)
commision= re.search(r'Коммисия:\s*(.+)', text)
total_price = re.search(r'Итог\s*(.+)', text)
bik= re.search(r'БИК:\s*(.+)', text)
oktmo = re.search(r'ОКТМО:\s*(.+)', text)

print()
print("Date:", date.group(1) if date else '-')
print('Amount:', amount.group(1) if amount else '-') 
print('Commision:', commision.group(1) if commision else '-')
print('Total Price:', total_price.group(1) if total_price else '-')
print('БИК:', bik.group(1) if bik else '-')
print('ОКТМО:', oktmo.group(1) if oktmo else '-')


# Pict Preprocessing 



# OCR + automatic Parsing



# receipt1.png 