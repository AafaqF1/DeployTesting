# imprting the file fastAPI and Win32com modules
import comtypes.client
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
class textToSpeech(BaseModel):
   text_input: str
app = FastAPI()
@app.post("/textToSpeech")
async def home(item:textToSpeech):
   item = jsonable_encoder(item)
   Speaker1 = item['text_input']
   speak = comtypes.client.CreateObject("SAPI.SpVoice")
   filestream = comtypes.client.CreateObject("SAPI.spFileStream")
   filestream.open("outputwin32com2.wav", 3, False, speed=False)
   speak.AudioOutputStream = filestream
   speak.Speak(Speaker1)
   filestream.close()
   response = {"file_url": f"http://127.0.0.1:8000/textToSpeech/outputwin32com2.wav"}
   return response