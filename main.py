#from fastapi import FastAPI
from services.openAi import findAiAnswer
from services.googleSearch import googleSearch
from services.soundAi import soundAi
from elevenlabs import stream
from services.videoApi import videoGeneration
from services.stockGen import StockContent
from services.streamToAudio import save_audio_stream
from services.mergeAudioVideo import merge_audio_video
import argparse
import asyncio


async def generateStockContent(topic):
    try:
        linkArray = googleSearch(topic)
        prompt = findAiAnswer(str(linkArray))
        audioStream = soundAi(prompt)

        # Creating mp4 and mp3 files
        StockContent(topic)
        save_audio_stream(audioStream , "../temp/output.wav")

#    Merging the audio and video files
    finally:
      merge_audio_video("../temp/video.mp4", "../temp/output.wav", "../temp/output.mp4")


async def generateContent(topic):

    linkArray = googleSearch(topic)
        
    prompt = findAiAnswer(str(linkArray))

    print(prompt)
    stream(soundAi(prompt))

    videoGeneration(prompt)

async def main():
    parser = argparse.ArgumentParser(description="Generate content for a video or stock content.")
    parser.add_argument("topic", type=str, help="Topic for the content")
    parser.add_argument(
        "--stock",
        action="store_true",
        help="Generate stock content (video + audio)",
    )
    args = parser.parse_args()

    if args.stock:
        await generateStockContent(args.topic)
    else:
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
    
