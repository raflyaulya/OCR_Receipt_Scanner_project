# first Deepseek api trial

from openai import OpenAI

deepseek_api_key = input('DeepSeek API key:\n')

client = OpenAI(
    api_key=deepseek_api_key,  # Ganti dengan API key asli
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
