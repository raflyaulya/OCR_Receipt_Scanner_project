from google import genai 
import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) 
GEMINI_API = os.getenv('GEMINI_API')

client = genai.Client(
    api_key= GEMINI_API
)

def model_response(question):
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=question
    )

    return response.text

quest = input('\nWanna ask something? \n') 
# explain how ai works in a few words only

ask_ai = model_response(question=quest)
print('result:\n', ask_ai)  