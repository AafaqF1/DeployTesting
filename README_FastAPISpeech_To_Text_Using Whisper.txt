Here's a step-by-step guide on how to create a FastAPI endpoint to convert speech to text using the Whisper library in PyCharm:

Install the required libraries:
 FastAPI, Whisper, and uvicorn. You can install them by running
 pip install fastapi whisper uvicorn in your command prompt/terminal.

Open PyCharm and create a new project.

In your PyCharm project, create a new Python file and name it app.py.

Import the required modules by adding the following code to your file:
from fastapi import FastAPI, File, UploadFile, Request, Response
import whisper
Initialize the FastAPI app and create an endpoint:

app = FastAPI()

# Loading Model
@app.Post("/Speech-to-Text")
asyn def Speech-to-Text(request:Request,file:UploadFile)

    model=whisper.load_model("base")
    # Transcribng the model into mp3 form
    result=model.transcribe("output1.mp3", fp16=False)
    # Response the Fast APi
    response = {"file_url": f"http://127.0.0.1:8000/textToSpeech/{result}"}
    return response
    Save the file and run it using the following command in your terminal/command prompt:

uvicorn app:app --reload
The endpoint will be available at http://localhost:8000/speech-to-text. You can use a tool like Postman to send a POST request to the endpoint with a .wav file as the payload.

When you run the endpoint and send a request to it with a .wav file, the audio file will be converted to text.