import os
import whisper
import json

model = whisper.load_model("small", device="cpu")

audios = os.listdir("audios")

for audio in audios:
    number = audio.split("_")[0]
    title = audio.split("_")[1][:-4]

    result = model.transcribe(audio=f"audios/{audio}", 
                                   language = "hi", 
                                   task = "translate",
                                   word_timestamps= False)
    
    chunks = []

    for chunk in result["segments"]:
        chunks.append({"video no": number,
                       "video title" : title, 
                       "start": chunk['start'],
                        "end": chunk["end"],
                        "text": chunk["text"]})
        
    metadata_chunk = {"chunk": chunks, "translation":result['text']}

    with open(f"json/{audio}.json", "w") as f:
        json.dump(metadata_chunk, f)
