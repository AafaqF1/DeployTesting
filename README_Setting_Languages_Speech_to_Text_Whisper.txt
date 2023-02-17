To convert speech to text using Whisper library in Python, you can follow these steps:

Install the Whisper library:
Copy code
pip install whisper
Import the library:
python

import whisper
Initialize the recognizer:
makefile
rec = whisper.WhisperRecognizer()
Start recording audio:

result=model.transcribe("output1.mp3", fp16=False,language="es-ES")
Note: Here is language