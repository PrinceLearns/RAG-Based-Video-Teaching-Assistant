# For our Project we need course videos we download it from youtube using this Program
#it will continue to download the whole playlist

import yt_dlp

url = "link for videos"  # Here I am using videos of "Code With Harray -- Sigma Web Development Course"

ydl_opts = {
    'format': 'best',
    'outtmpl': 'videos/%(title)s.%(ext)s',

    #'noplaylist': True  # --for one video
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

