# core/ocr_utils.py
import pytesseract
from PIL import Image
import io
from core.config import TESSERACT_CMD, OCR_LANG

def extract_text_from_image(image_bytes: bytes) -> str:
    """Runs OCR on image bytes and returns extracted text."""
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image, lang=OCR_LANG)
    return text.strip()
