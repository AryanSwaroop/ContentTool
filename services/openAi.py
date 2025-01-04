import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def findAiAnswer(prompt : str):
  client = OpenAI(
    api_key = os.getenv('openAiKey')
  )

  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "user", "content": prompt}
    ]
  )

  print(completion.choices[0].message.content)
  return completion.choices[0].message.content 



