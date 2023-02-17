import whisper
from langdetect import detect
model=whisper.load_model("base")
result=model.transcribe("hello Spenish.mp3", fp16=False)
FinalText=result['text']
# with open("textfile.txt", "w") as file:
#     file.write(result["text"])
print(FinalText)
def detect_language(FinalText):
        return detect(FinalText)
language = detect_language(FinalText)
print("The language of the text is:", language)