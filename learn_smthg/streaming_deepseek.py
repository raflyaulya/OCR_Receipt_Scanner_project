# Streaming

from openai import OpenAI

api_key = input('DeepSeek API KEY:\n')

client = OpenAI(api_key=api_key,
                base_url='https://api.deepseek.com')


messages = [{'role':'user', 'content': '9.11 and 9.8, which is greater?'}]
response = client.chat.completions.create(
    model='deepseek-reasoner',
    messages=messages, 
    stream=True
)

reasoning_content = ''
content =''

for chunk in response: 
    if chunk.choices[0].delta.reasoning_content: 
        reasoning_content += chunk.choices[0].delta.reasoning_content 
    else:
        content += chunk.choices[0].delta.content

# reasoning_content = response.choices[0].message.reasoning_content 
# content = response.choices[0].message.content

# print('\n=======================================================\n')
# print('Here below is the Reasoning content:\n')
# print(reasoning_content)
# print('\n=======================================================\n')
# print('Here below is the answer content:\n')
# print(reasoning_content)

# # print('\n=======================================================\n')
# print('\n=======================================================\n')