Here's a step-by-step guide on how to create a FastAPI endpoint to convert text to speech using Python in PyCharm:

Install the required libraries: FastAPI, pyttsx3, and uvicorn. You can install them by running
pip install fastapi pyttsx3 uvicorn in your command prompt/terminal.

Open PyCharm and create a new project.

In your PyCharm project, create a new Python file and name it app.py.

Import the required modules by adding the following code to your file:

from fastapi import FastAPI, Request, Response
import pyttsx3

Initialize the FastAPI app and create an endpoint:

app = FastAPI()

@app.post("/text-to-speech")
async def text_to_speech(request: Request, text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return {"message": "Text to speech conversion successful"}
Save the file and run it using the following command in your terminal/command prompt:


uvicorn app:app --reload
The endpoint will be available at http://localhost:8000/text-to-speech. You can use a tool like Postman to send a POST request to the endpoint with a JSON payload containing the text that you want to be converted to speech.

When you run the endpoint and send a request to it, the text that you send in the request body will be converted to speech.

Now instructions for Male and Female voice in text to speech



