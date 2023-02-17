Create the FastAPI endpoint:
Here is a Python script to create the FastAPI endpoint to convert the speech file into text and detect its language:
Importing the libraries
from fastapi import FastAPI, File, UploadFile
from langdetect import detect
import whisper
app = FastAPI()
@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile):
    # Loading Model
    model = whisper.load_model("base")
    result = model.transcribe("hello Spenish.mp3", fp16=False)
    FinalText = result['text']
    # with open("textfile.txt", "w") as file:
    #     file.write(result["text"])
    print(FinalText)

    def detect_language(FinalText):
        return detect(FinalText)

    language = detect_language(FinalText)
    print("The language of the text is:", language)
    response = {"file_url": f"http://127.0.0.1:8000/textToSpeech/{result}"}
    return response

Run the FastAPI app:
To run the FastAPI app, you can run the following command in your PyCharm terminal:
uvicorn main:app --reload

