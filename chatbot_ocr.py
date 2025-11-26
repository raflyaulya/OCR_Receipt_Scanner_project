import telebot
from PIL import Image 
import pytesseract
import io
from openai import OpenAI
from dotenv import *
import os 

load_dotenv(find_dotenv())

# chatbot Telegram API key
TELEGRAM_API = os.getenv('TELEGRAM_API') 
DEEPSEEK_API = os.getenv('DEEPSEEK_API')

bot = telebot.TeleBot(TELEGRAM_API)

client = OpenAI(api_key=DEEPSEEK_API,
                base_url='https://api.deepseek.com/v1')


# define a command handler 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to theRaf OCR Receipt Scanner!\nType /info to get more information.')

# command /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Need some help? Please tell me anything need here below')
    
# for /info command
@bot.message_handler(commands=['info'])
def send_info(message):
    add_msg = 'How can I help you today sir?' 
    bot.reply_to(message, f'This is a simple Telegram bot implemented in Python. \n\n{add_msg}')


# === FUNCTION ANALISIS ===
def analyze_with_deepseek(text):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",   # reasoner hasilnya jelek!!
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
                {"role": "user", 
                 "content": f"Analyze the following receipt text and then please write the output as 4 formats (Store, Date, Address, Total) only! No explanation, no extra notes! \n\n{text}"}  
            ],
            # temperature=0.2, # lebih rendah lebih baik!
            temperature=0.7, # lebih rendah lebih baik!
            max_tokens=300  # embedding lebih berguna disini, to find the better max tokens 
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[DeepSeek ERROR] {e}"

# Upload any pict/photo here!
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # get the pict/photo 
        file_info = bot.get_file(message.photo[-1].file_id) 
        downloaded_file = bot.download_file(file_info.file_path)  
        # convert into pict 
        image = Image.open(io.BytesIO(downloaded_file))  
        # run the OCR 
        # lang_opt = 'ind+eng+jpn'
        lang_opt = 'ind+eng+rus'
        # ind+eng+jpn

        text = pytesseract.image_to_string(image, lang=lang_opt)

        if not text.strip():
            bot.reply_to(message, 'We got the pict! but unfortunately we can\'t detected the text ☹️')
            return 
        # analyze with Deepseek 
        bot.reply_to(message, 'Please wait!\nПодаждите пожалуйста!')
        # send the OCR output to user 
        result = analyze_with_deepseek(text) 
        # bot.reply_to(message, f'Here below your analyzing output:\n\n{result}')
        bot.reply_to(message, f"{result}")
    except Exception as e:
        bot.reply_to(message, f'Something wrong just happened :(\n{e}')


#Define a message handler 
@bot.message_handler(func=lambda message:True) 
def echo_all(message):
    bot.reply_to(message, f'Lo menulis: {message.text}')


# Start the bot
print('Bot is running...')
bot.polling()