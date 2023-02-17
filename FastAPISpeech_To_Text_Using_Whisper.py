from fastapi import FastAPI, File, UploadFile
import whisper
app = FastAPI()

@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile):
    # Loading Model
    model=whisper.load_model("base")
    result=model.transcribe("speech.mp3", fp16=False)
    response = {"file_url": f"http://127.0.0.1:8000/textToSpeech/{result}"}
    return response
