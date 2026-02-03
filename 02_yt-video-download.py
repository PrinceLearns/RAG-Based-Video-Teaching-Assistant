# For our Project we need course videos we download it from youtube using this Program
#it will continue to download the whole playlist

import yt_dlp

url = "https://www.youtube.com/watch?v=tVzUXW6siu0&list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w&index=1"

ydl_opts = {
    'format': 'best',
    'outtmpl': 'videos/%(title)s.%(ext)s',

    #'noplaylist': True  # --for one video
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
