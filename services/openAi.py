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
      {"role": "user", "content": prompt + "These are the links i found for you now make an all text script for a reel , make it a single paragraph of words woth no scene or other things."}
    ]
  )

  return completion.choices[0].message.content 



