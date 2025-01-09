from moviepy import VideoFileClip, concatenate_videoclips, AudioFileClip


def merge_audio_video(videofile, audiofile, outputfile):
    # Load video and audio
    video = VideoFileClip(videofile)
    audio = AudioFileClip(audiofile)
    audio_duration = audio.duration

    # Repeat video to match or exceed the audio duration
    if video.duration < audio_duration:
        loops = int(audio_duration // video.duration) + 1
        repeated_clips = [video] * loops  # Repeat video
        video = concatenate_videoclips(repeated_clips)  # Combine repeated clips
        video = video.subclip(0, audio_duration)  # Trim to audio duration

    # Set the audio to the video
    video = video.set_audio(audio)

    # Export the final video
    video.write_videofile(outputfile, codec="libx264", audio_codec="aac")