# Here we are using the openai whisper Model .
# but it is slow if you want faster use openai's api

# it is slow so we cannot directly use on the our big audio files we need small files for making the structure of chunks.
#we using sample.mp3 10sec audio file for that

import whisper
import json

model = whisper.load_model("small", device="cpu")

#for traslation use any model except turbo

result = result = model.transcribe(audio="Sample.mp3", 
                                   language = "hi", 
                                   task = "translate",
                                   word_timestamps= False)

chunks = []

for chunk in result["segments"]:
    chunks.append({"start": chunk['start'],
                   "end": chunk["end"],
                   "text": chunk["text"]})
    
with open("output.json", "w") as f:
    json.dump(chunks, f)