# bot/chatbot_handler.py
import telebot
from core.config import TELEGRAM_API
from core.ocr_utils import extract_text_from_image
from core.llm_utils import analyze_with_deepseek, analyze_with_gemini_simple
import os 
import time

bot = telebot.TeleBot(TELEGRAM_API)

# =====     START handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to theRaf OCR Receipt Scanner!\nType /info to get more information.")

# =====     HELP handler
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Need some help? Please tell me anything need here below")

# =====     INFO handler
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "This is a simple Telegram bot implemented in Python using OCR and LLM.")

# =====     STOP handler
@bot.message_handler(commands=['stop'])
def stop_session(message):
    bot.reply_to(message, "Session ended, See you next time! \nbye-bye!")
    time.sleep(0.3)
    os._exit(0)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        text = extract_text_from_image(downloaded_file)
        if not text:
            bot.reply_to(message, "We got the pict! but unfortunately we can’t detect any text ☹️")
            return

        bot.reply_to(message, "Please wait!\nПодаждите пожалуйста!")
        # result = analyze_with_deepseek(text)  # using Deepseek LLMs
        result = analyze_with_gemini_simple(text)    # using GEMINI LLMs
        bot.reply_to(message, f"{result}")
        followup_text = (
        "✅ *Analysis completed!*\n\n"
        "You can continue with one of the following options:\n"
        "• /info — Learn more about this bot\n"
        "• /help — Need assistance?\n"
        "• /stop — End the session for now\n\n"
        "_Thank you for using theRaf OCR Scanner 🧾_\n"
        "We hope this helps you manage your spending better!")
        bot.send_message(message.chat.id, followup_text, parse_mode='Markdown') 

    except Exception as e:
        bot.reply_to(message, f"Something wrong just happened :(\n{e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Lo menulis: {message.text}")
