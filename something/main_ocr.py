from PIL import Image
import pytesseract
import os 

# SET PATH TO tesseract.exe 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load pict 
# image = Image.open('D:\python_learning_in_transisition_time\cek1.png')
# image = Image.open('struk\strukBelanja3.jpg')
image = Image.open('trilingual.png')

lang_opt = input('What languages?\n')
# ind+eng+jpn 

# OCR: ambil text dari gambar 
# text = pytesseract.image_to_string(image, lang='eng+rus')
text = pytesseract.image_to_string(image, lang=lang_opt)
get_lang = pytesseract.get_languages(config='')

# tampilkan hasil 
print('\n========================== HASIL OCR ==========================\n') 
# print('what languages i can have: ',get_lang)
# print() 
print(text, "\n========================== end of OCR ==========================")  
# print('========================== end of OCR ==========================\n') 
