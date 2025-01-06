from fastapi import FastAPI
from services.openAi import findAiAnswer
from services.googleSearch import googleSearch
from services.soundAi import soundAi


def generateContent(topic):
    linkArray = googleSearch(topic)
    prompt = findAiAnswer(str(linkArray))

    print(prompt)


generateContent("freelancers of india")



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
    
