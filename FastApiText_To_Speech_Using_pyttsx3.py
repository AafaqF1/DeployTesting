from fastapi import FastAPI
import pyttsx3
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
class TextToSpeech(BaseModel):
    text_input: str
app = FastAPI()
engine = pyttsx3.init()
@app.post("/textToSpeech/")
async def home(item:TextToSpeech):
    item = jsonable_encoder(item)
    print(item)
    text_input = item['text_input']
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    volume = engine.getProperty("volume")
    engine.setProperty("volume", 1)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text_input)
    output="output.mp3"
    engine.save_to_file(engine.say, output)
    engine.runAndWait()
    engine.stop()
    response = {"file_url": f"http://127.0.0.1:8000/textToSpeech/{output}"}
    return response