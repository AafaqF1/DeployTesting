To change the voice of a text-to-speech conversion using the Whisper library in Python in PyCharm,
 you will need to make use of the voice parameter when calling the say() method.
 The available voices depend on the underlying TTS engine that you are using. For example,
 if you are using the default TTS engine, espeak, you can use the following code to change the voice:

 import whisper

# Initialize the TTS engine
engine = whisper.Whisper()

# Set the voice to male
engine.voice = "m3"
engine.say("This is a male voice")

# Set the voice to female
engine.voice = "f4"
engine.say("This is a female voice")
Note that the exact list of available voices will depend on your installation and the TTS engine you are using.
You can consult the documentation of the TTS engine to find out more information.
