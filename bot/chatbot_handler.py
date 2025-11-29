# bot/chatbot_handler.py
import telebot
# from core.config import TELEGRAM_API
from bot import bot
from core.ocr_utils import extract_text_from_image
from core.llm_utils import analyze_with_deepseek #analyze_with_gemini_simple
import os 
import time

# bot = telebot.TeleBot(TELEGRAM_API, p)

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


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Lo menulis: {message.text}")
