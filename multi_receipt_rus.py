
import pytesseract
from PIL import Image
import re
import os
from openai import OpenAI

# Konfigurasi Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

api_key = input('Deepseek API key:\n') 

# Inisialisasi DeepSeek Client
client = OpenAI(
    api_key = api_key,  # Ganti dengan API key Anda
    base_url="https://api.deepseek.com/"
)

# Direktori berisi gambar struk
invoice_dir = "invoice_pict"

def extract_text_from_image(image_path):
    """Extract text from receipt images"""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='rus+eng')
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def analyze_with_deepseek(text):
    """Use DeepSeek API to analyze receipt text"""
    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": """
                You are a receipt analysis expert. Your tasks:
                    1. Identify the store/date/total purchase
                    2. Extract the address (if applicable)
                    3. Format the output as:
                    Store: [store name]
                    Date: [date]
                    Address: [address]
                    Total: [total payment]
                """},
                {"role": "user", "content": f"Analyze the following receipt text:\n\n{text}"}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"DeepSeek API error: {e}")
        return None

def print_formatted_result(result_text, fname):
    """Prints the results in the requested format"""
    print(f"\n========== Analysis result {fname} ==========")
    print(result_text)
    print("=" * 40)

# Proses semua gambar struk dalam direktori
for fname in sorted(os.listdir(invoice_dir)):
    if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(invoice_dir, fname)
        
        # Ekstrak teks dari gambar
        text = extract_text_from_image(image_path)
        if not text:
            print(f"\n========== Failed to processing {fname} ==========")
            continue
        
        # analyzing with deepseek 
        analysis_result = analyze_with_deepseek(text)
        
        if analysis_result:
            print_formatted_result(analysis_result, fname)
        else:
            print(f"\n========== Failed to processing {fname} ==========")