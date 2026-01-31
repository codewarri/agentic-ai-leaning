from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.1.106:1234/v1",
    api_key="not-needed"
)

completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": "what do u knew about japan"}
    ],
    temperature=0.7,
)

print(completion.choices[0].message.content)
