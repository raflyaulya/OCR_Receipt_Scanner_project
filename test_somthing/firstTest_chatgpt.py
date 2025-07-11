# first Deepseek api trial
# sk-fe1b91723bc7450ba1edc6c924830a1b   ||    auliarafli819@gmail.com    (( VALID!!!! ))
# sk-c8bfc92818a949e5b9a58e2d185e1b89   ||    nasutionrafly575@gmail.com

from openai import OpenAI

client = OpenAI(
    api_key="sk-fe1b91723bc7450ba1edc6c924830a1b",  # Ganti dengan API key asli
    base_url="https://api.deepseek.com/v1"           # Gunakan /v1 untuk kompatibilitas
)

askChat_DeepSeek = 'a short way to introduce myself in spanish language!'

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant and Please answer only what is asked & just short answer!"},
        # {"role": "user", "content": "Hello, do you know who am I?"}
        {"role": "user", "content": askChat_DeepSeek}
    ],
    stream=False
)

print('\n========================================================\n')
print(response.choices[0].message.content)
print('\n========================================================')

# ===================================================================================================================
# ====================              DEEPSEEK Reasoner       ====================              
