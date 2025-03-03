from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
print("hello")
print(completion.choices[0].message.content)
print("bye")
