# No Streaming

from openai import OpenAI

deepseek_api_key = input('Deepseek API key:\n')

client = OpenAI(api_key=deepseek_api_key,
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