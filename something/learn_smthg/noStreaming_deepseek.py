# No Streaming

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os 

load_dotenv(find_dotenv())
DEEPSEEK_API = os.getenv('DEEPSEEK_API')

client = OpenAI(api_key=DEEPSEEK_API,
                base_url='https://api.deepseek.com')


messages = [{'role':'user', 'content': '9.11 and 9.8, which is greater?'}]
response = client.chat.completions.create(
    model='deepseek-reasoner',
    messages=messages
)

reasoning_content = response.choices[0].message.reasoning_content 
content = response.choices[0].message.content

print('\n=======================================================\n')
print('Here below is the Reasoning content:\n')
print(reasoning_content)
print('\n=========================================================================================================')
print('=========================================================================================================\n')
print('Here below is the answer content:\n')
print(content)

# print('\n=======================================================\n')
print('\n=======================================================\n')