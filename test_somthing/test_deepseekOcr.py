# sk-fe1b91723bc7450ba1edc6c924830a1b   ||    auliarafli819@gmail.com    (( VALID!!!! ))

from PIL import Image
import pytesseract
import requests
import os 
from openai import OpenAI


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Langkah 1: Ekstrak teks dengan OCR
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='ind+eng')  # Pastikan Tesseract terinstall
    return text

# Langkah 2: Proses teks dengan DeepSeek
def query_deepseek(api_key, extracted_text):
    base_url = "https://api.deepseek.com/v1/chat/completions"
    # base_url = "https://api.deepseek.com/v1"
    headers = {"Authorization": f"Bearer {api_key}"}
    ask_prompt = f"""
    Dari struk berikut, ekstrak informasi berikut dalam format JSON:
    - Nama Toko
    - Alamat
    - Total belanja
    - Tanggal transaksi
    
    Teks struk: {extracted_text}
    """
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": ask_prompt},
            {"role": "user", "content": "You are a helpful assistant & Please answer only what is asked!"}
            ]
    }
    response = requests.post(base_url, json=data, headers=headers)
    # return response.json()
    return response

# Contoh penggunaan
image_path = "strukbelanja.jpg"  # pict of struk belanja
extracted_text = extract_text_from_image(image_path)
api_key = "sk-fe1b91723bc7450ba1edc6c924830a1b"
result = query_deepseek(api_key, extracted_text)
print(result)