# We are going to Convert video format to mp3

import os
import subprocess

files = os.listdir("videos")


for file in files:
    file_no = file.split("#")[1].split(".")[0]
    file_name = file.split(" ｜ ")[0]

    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{file_no}_{file_name}.mp3"])
