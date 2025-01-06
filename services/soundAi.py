import os
from elevenlabs import stream
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

def soundAi(prompt):
  client = ElevenLabs(
    api_key=os.getenv('elevenLabs')
  )

  audio_stream = client.text_to_speech.convert_as_stream(
      text=prompt,
      voice_id="JBFqnCBsd6RMkjVDRZzb",
      model_id="eleven_multilingual_v2"
  )

  return audio_stream

