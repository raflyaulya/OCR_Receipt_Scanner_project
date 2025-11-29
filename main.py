# main.py
from bot.chatbot_handler import bot
from telebot import types
from fastapi import FastAPI, Request
from core.config import *

app = FastAPI() 

@app.get('/')
async def home():
    return {'status': 'Okay', 
            'message': 'theRaf OCR Receipt Scanner via Webhook is running!'}


@app.on_event('startup')
async def startup_event():
    if not BASE_URL:
        print("BASE_URL is not  set. Please set it in the .env file.")
        return
    
    webhook_url = f"{BASE_URL}/webhook"
    print('Setting webhook to:', webhook_url)
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)


# endppoint for calling the Telegram 
@app.post(f"/webhook")
async def telegram_webhook(request: Request):
    """Endpoint to receive updates from Telegram via webhook."""
    try:
        json_data = await request.json()
        update = types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return {'status': 'success', 
                'message': 'everything is fine!'}
    except Exception as e:
        print(f"Error processing update: {e}")
        return {'status': 'error', 
                'message': str(e)}






# if __name__ == "__main__":
#     print("Bot is running...")
#     bot.polling()
