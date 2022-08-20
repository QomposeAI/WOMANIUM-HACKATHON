import moviepy.editor

#declaring the path of video file--> will be changed into client provided video in future
video=moviepy.editor.VideoFileClip('demo.mp4')

audio=video.audio

audio.write_audiofile('extracted_audio.mp3')