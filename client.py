from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
