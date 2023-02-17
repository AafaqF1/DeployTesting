import pyttsx3
engine = pyttsx3.init()
from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/")
async def create_file():
    file_path = "me.txt"
    with open(file_path, "r") as f:
       g= f.read()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    volume = engine.getProperty("volume")
    print("volume is {0}".format(volume))
    engine.setProperty("volume", 1)
    voices = engine.getProperty("voices")
    print("Female Voice : {0}".format(voices[1].id))
    engine.setProperty("voice", voices[1].id)
    engine.say("me")
    engine.say("1. “Lamb to the Slaughter” by Roald Dahl While not exactly a philosophical or political tale like our first two examples,")
    engine.save_to_file(engine.say, '5_TheShortStories.mp3')
    engine.runAndWait()
    engine.stop()
    return {"file_url": f"http://localhost:8000/{file_path}"}