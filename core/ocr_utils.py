# core/ocr_utils.py
import pytesseract
from PIL import Image
import io
# from bot.chatbot_handler import bot 
from bot import bot
from core.llm_utils import analyze_with_deepseek
# from llm_utils import analyze_with_deepseek
from core.config import *


@bot.message_handler(content_types=['photo'])
def extract_text_from_image(image_bytes):
    try:
        """Runs OCR on image bytes and returns extracted text."""
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
        # get the pict/photo 
        file_info = bot.get_file(image_bytes.photo[-1].file_id) 
        downloaded_file = bot.download_file(file_info.file_path)

        image = Image.open(io.BytesIO(downloaded_file))
        # lang_opt = OCR_LANG
        text_result = pytesseract.image_to_string(image, lang=OCR_LANG)

        if not text_result.strip():
            bot.reply_to(image_bytes, "We got the pict! but unfortunately we can’t detect any text ☹️")
            return 
        
        bot.reply_to(image_bytes, 'Please wait!') 

        # TAMBAHAN / EDITING 
        result = analyze_with_deepseek(text_result)
        bot.reply_to(image_bytes, f"{result}")

        followup_text = (
        "✅ *Analysis completed!*\n\n"
        "You can continue with one of the following options:\n"
        "• /info — Learn more about this bot\n"
        "• /help — Need assistance?\n"
        "• /stop — End the session for now\n\n"
        "_Thank you for using theRaf OCR Scanner 🧾_\n" 
        "We hope this helps you manage your spending better!")
        bot.send_message(image_bytes.chat.id, followup_text, parse_mode='Markdown')

    except Exception as e: 
        bot.reply_to(image_bytes, f"something wrong just happened bro :( \n{e}") 
        # return text.strip()


