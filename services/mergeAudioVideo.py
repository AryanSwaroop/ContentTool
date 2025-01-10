import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def merge_audio_video(videofile, audiofile, outputfile):
    with VideoFileClip(videofile) as video, AudioFileClip(audiofile) as audio:
        audio_duration = audio.duration

        # Repeat video to match or exceed the audio duration
        if video.duration < audio_duration:
            loops = int(audio_duration // video.duration) + 1
            repeated_clips = [video] * loops
            video = concatenate_videoclips(repeated_clips)

        # Trim video to exactly match the audio duration
        video = video.subclip(0, audio_duration)

        # Set audio to video
        final_video = video.set_audio(audio)

        # Export the final video
        final_video.write_videofile(outputfile, codec="libx264", audio_codec="aac")
        print(f"Video saved to {outputfile}")

        # Play the video using default media player
        os.system(f"start {outputfile}")  # For Windows
