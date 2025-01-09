import os
import requests
from dotenv import load_dotenv

load_dotenv()

def StockContent(searchQuery : str):

    videoarray = []

    api_key = os.getenv('pixelsApi')
    url = "https://api.pexels.com/videos/search?query=" + searchQuery + "&per_page=1"

    headers = {
        "Authorization": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for video in data.get('videos')[0].get('video_files'):
            videoarray.append(video.get('link'))
        print(videoarray)
    else:
        print(f"Error: {response.status_code}")

    os.makedirs(os.path.dirname("../temp/video.mp4"), exist_ok=True)

    download_mp4(videoarray[1] , "../temp/video.mp4")

    return videoarray[1]



# Download the video file and save it at temp file.
def download_mp4(url, save_path):
    try:
        print("Downloading...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        print(f"Download completed and saved to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



    
