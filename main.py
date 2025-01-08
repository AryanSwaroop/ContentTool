#from fastapi import FastAPI
from services.openAi import findAiAnswer
from services.googleSearch import googleSearch
from services.soundAi import soundAi
from elevenlabs import stream
from services.videoApi import videoGeneration
import argparse
import asyncio



async def generateContent(topic):

    linkArray = googleSearch(topic)
        
    prompt = findAiAnswer(str(linkArray))

    print(prompt)
 #   stream(soundAi(prompt))

    videoGeneration(prompt)

async def main():
    parser = argparse.ArgumentParser(description='Generate content for a video with topic')
    parser.add_argument('topic', type=str, help='Topic for the video')
    args = parser.parse_args()
    await generateContent(args.topic)


if __name__ == "__main__":
    asyncio.run(main())


# from pydantic import BaseModel

# app = FastAPI()

# class promptObject(BaseModel):
#     promptQ: str

# class answerObject(BaseModel):
#     ans: str

# @app.get("/")
# async def root():
#     return { "data" : "Main port"}

# @app.post("/generate/", response_model=answerObject)
# async def generate_answer(user: promptObject):

#     try:
#         answer = findAiAnswer(user.promptQ)
#         return answerObject(ans=answer)
    
#     except Exception as e:
#         print(str(e))
#         return str(e)
    
