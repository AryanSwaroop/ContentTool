import os
import requests
import datetime
from dotenv import load_dotenv
import webbrowser

load_dotenv()

def videoGeneration(scriptText : str):

    url = "https://tavusapi.com/v2/videos"

    payload = {
        "replica_id": "r79e1c033f",
        "script": scriptText,
        "video_name": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "generated",
    }
    headers = {
        "x-api-key": os.getenv('TavusIoApi'),
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

    try:
      webbrowser.open(response.text.hosted_url)
    except Exception as e:  
      print(str(e))