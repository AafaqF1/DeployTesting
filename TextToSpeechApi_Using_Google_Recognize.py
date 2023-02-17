from fastapi import FastAPI, File, UploadFile

app = FastAPI()
@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile):
    recognizer = Recognizer()
    with AudioFile(file.file) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return {"text": text}