import os

def save_audio_stream(audio_stream_url, output_audio_path):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
        
        # Save the stream as a WAV or MP3 file
        with open(output_audio_path, "wb") as audio_file:
            for chunk in audio_stream_url:
                audio_file.write(chunk)
        
        print(f"Audio stream saved to {output_audio_path}")
    except Exception as e:
        print(f"Error saving audio stream: {e}")
