# first Deepseek api trial
# sk-fe1b91723bc7450ba1edc6c924830a1b   ||    auliarafli819@gmail.com    (( VALID!!!! ))
# sk-c8bfc92818a949e5b9a58e2d185e1b89   ||    nasutionrafly575@gmail.com

from openai import OpenAI
import os

# api_key = input('Input your API KEY here below:\n')

client = OpenAI(
    # api_key=api_key,  # Ganti dengan API key asli
    api_key="sk-fe1b91723bc7450ba1edc6c924830a1b",  # Ganti dengan API key asli
    base_url="https://api.deepseek.com/v1"           # Gunakan /v1 untuk kompatibilitas
)

ask_DeepSeek = 'a short way to introduce myself in russian!'

response = client.chat.completions.create(
    model="deepseek-chat",    # deepseek-chat
    messages=[
        {"role": "system", "content": "You are a helpful assistant!"},
        # {"role": "system", "content": "You are a helpful assistant and Please answer only what is asked & just short answer!"},
        {"role": "user", "content": ask_DeepSeek}
    ],
    stream=False
)

print('\n========================================================\n')
print(response.choices[0].message.content)
print('\n========================================================')

# ===================================================================================================================
# ====================              DEEPSEEK Reasoner       ====================              

# from openai import OpenAI
# client = OpenAI(api_key="sk-fe1b91723bc7450ba1edc6c924830a1b", base_url="https://api.deepseek.com")

# # Round 1
# messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
# response = client.chat.completions.create(
#     model="deepseek-reasoner",
#     messages=messages
# )

# reasoning_content = response.choices[0].message.reasoning_content
# content = response.choices[0].message.content