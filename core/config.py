import os 
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv()) 

DEEPSEEK_API = os.getenv('DEEPSEEK_API') 
TELEGRAM_API = os.getenv('TELEGRAM_API') 
GEMINI_API = os.getenv('GEMINI_API')

# language setting
OCR_LANG = 'ind+eng' 

# path to Tesseract 
TESSERACT_CMD =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# LLMs deepseek base url 
DEEPSEEK_BASE_URL = 'https://api.deepseek.com/v1' 