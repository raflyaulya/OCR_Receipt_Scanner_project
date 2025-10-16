import cv2 
import pytesseract 
import re 
from PIL import Image

# ==============        STEP 1: PREPROCESSING   =====================
# img = cv2.imread('receipt1.jpg')

# # Grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Thresholding
# _, thresh= cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# # Noise Removal 
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
# opening= cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) 

# # save hasil
# cv2.imwrite('preprocessed_receipt.png', opening) 

# ==============        STEP 2: OCR + REGEX PARSING    =====================
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# image = Image.open('preprocessed_receipt.png')
# img = cv2.imread('receipt1.jpg')
image = Image.open('struk/strukBelanja5.jpg')
text = pytesseract.image_to_string(image, lang='ind') 
get_lang = pytesseract.get_languages(config='')


print(text)
# # contoh Parsing 
# date = re.search(r'Tanggal:\s*(.+)', text)
# ppn = re.search(r'PPN=\s*(.+)', text)
# tunai = re.search(r'TUNAI :\s*(.+)', text)
# saving_back = re.search(r'ANDA HEMAT :\s*(.+)', text)
# total_price = re.search(r'TOTAL\s*(.+)', text)
# # bik= re.search(r'БИК:\s*(.+)', text)

# print()
# print("Date:", date.group(1) if date else '-')
# print('PPN:', ppn.group(1) if ppn else '-') 
# print('TUNAI :', tunai.group(1) if tunai else '-') 
# print('Saving money:', saving_back.group(1) if saving_back else '-')
# # print('Total Price:', total_price.group(1) if total_price else '-')
# print('Total Price:', total_price if total_price else '-')
# # print('БИК:', bik.group(1) if bik else '-')


# Pict Preprocessing 



# OCR + automatic Parsing



# receipt1.png 