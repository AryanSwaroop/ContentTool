from io import BytesIO
from pydub import AudioSegment

def convert_to_mp3(audio_stream, filename):
    try:
        # Step 1: Convert the generator stream to a BytesIO object
        audio_content = b''.join([chunk for chunk in audio_stream])
        audio_stream = BytesIO(audio_content)

        # Step 2: Ensure the input stream is at the start
        audio_stream.seek(0)

        # Step 3: Load the audio into pydub (assumes the format is 'wav')
        audio = AudioSegment.from_file(audio_stream, format="wav")
        
        # Step 4: Create a BytesIO stream for MP3
        mp3_stream = BytesIO()
        audio.export(mp3_stream, format="mp3")
        mp3_stream.seek(0)  # Reset to the start of the stream

        # Step 5: Save MP3 to file
        save_mp3(mp3_stream, filename)

        return filename  # Returning the file path

    except Exception as e:
        print(f"Error during conversion: {e}")

# Save the MP3 to file
def save_mp3(mp3_stream, filename="../temp/output.mp3"):
    try:
        with open(filename, "wb") as f:
            f.write(mp3_stream.getvalue())
        print(f"MP3 saved as {filename}")
    except Exception as e:
        print(f"Error saving MP3: {e}")
