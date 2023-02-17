Install the required libraries:
In your PyCharm terminal, run the following commands to install the Whisper and langdetect libraries:

pip install langdetect
pip install whisper
Here is a step-by-step guide on how to convert speech to text in Python using the Whisper library in PyCharm:
Installation

Install the Whisper library: Open the terminal in PyCharm and type in the following command to install the Whisper library:
pip install whisper
Importing and Creating Function

Import the library: In your Python code, add the following line to import the Whisper library:
import whisper

Record audio: Use the whisper.record function to record audio. For example, the following code will record 5 seconds of audio and save it as a wav file:
Program
1
audio = whisper.record(duration=5)
audio.export("recording.wav", format="wav")
Transcribe the audio: Use the whisper.Transcriber class to transcribe the recorded audio. For example, the following code will transcribe the audio file we just recorded and print the transcribed text:
2
transcriber = whisper.Transcriber("recording.wav")
result = transcriber.transcribe()
Final Text=(result.text)

Importing the function
Detect the language of the text:
Here is a Python script to detect the language of the text using the langdetect library:

from langdetect import detect

def detect_language(Final Text):
    return detect(text)

language = detect_language(Final Text)
print("The language of the text is:", language)
Combine these two scripts to get the complete solution
 to convert a speech file into text and detect its language in PyCharm.




