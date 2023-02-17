Here's a step-by-step guide on how to convert speech to text
using the Google recognizer library in Python:

Installation

Install the Google Cloud Speech-to-Text library by running
pip install google-cloud-speech in your command prompt/terminal.
pip install fastAPI(If you want to create Fast API)
Create a Google Cloud account and set up a project in the Google Cloud Console to get a service account key.

Store the service account key as a JSON file.

Set up authentication for the Google Cloud Speech-to-Text API by running the following code in your Python environment:
import
 from fastapi import FastAPI, File, UploadFile
from speech_recognition import Recognizer, AudioFile
INitializing FastAPI

app = FastAPI()

 Adding Post Methode api

@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile):
    recognizer = Recognizer()
    with AudioFile(file.file) as source:
        audio = recognizer.record(source)

 Applying the Google Api for Convert Speech to Text

    text = recognizer.recognize_google(audio)

     Returing the text file

    return {"text": text}