import os 
from dotenv import * 
import telebot 

load_dotenv(find_dotenv()) 

TELEGRAM_API = os.getenv('TELEGRAM_API')

if not TELEGRAM_API:
    raise ValueError("Oops.. \nthe TELEGRAM_API key not found in environment variables.")

bot = telebot.TeleBot(TELEGRAM_API, parse_mode='HTML')
