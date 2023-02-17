# Import Whisper
import whisper
# Loading Model
model=whisper.load_model("base")
# Transcribng the model into mp3 form
result=model.transcribe("output1.mp3", fp16=False)
print(result['text'])
# Make text File
with open("textfile.txt", "w") as file:
    file.write(result["text"])

