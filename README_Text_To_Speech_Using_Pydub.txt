Here's how you can convert a text file to speech in Python using the pydub library in PyCharm,
and also change the language and pitch of the speech:
Installation
Install pydub library: Open the terminal in PyCharm and type the following command to install pydub:
 pip install pydub.
Importing and Creatig Fuction
Import the library: In your Python code, add the following import statement:
from pydub import AudioSegment.

Read the text file: Use the open method to read the text file and convert it to a string.

with open("textfile.txt", "r") as file:
    text = file.read()
Convert text to speech:
To convert text to speech using pydub, you need to use the from_wav method,
 which creates an audio segment from a WAV file. You can use the gTTS library to convert the text to speech,
 and then save the result to a WAV file.
Here's an example code to convert text to speech using the gTTS library and save the result to a WAV file:

from gtts import gTTS
from pydub import AudioSegment

text = "Hello, this is an example of text to speech conversion."
tts = gTTS(text, lang='en')
tts.save("hello.mp3")

audio = AudioSegment.from_mp3("hello.mp3")
audio.export("hello.wav", format="wav")
Change language and pitch: To change the language and pitch of the speech,
you can use the lang and slow arguments of the gTTS constructor, respectively.
The lang argument accepts the language code for the desired language, and the slow argument changes the speed of the speech.
Here's an example code to convert text to speech in French with a lower pitch:

from gtts import gTTS
from pydub import AudioSegment

text = "Bonjour, ceci est un exemple de conversion de texte en voix."
tts = gTTS(text, lang='fr', slow=True)
tts.save("bonjour.mp3")

audio = AudioSegment.from_mp3("bonjour.mp3")
audio.export("bonjour.wav", format="wav")

Play the speech: You can play the speech using the play method of the audio segment. Here's an example:

from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav("hello.wav")
play(audio)
This is just a basic example of how you can use pydub to convert text to speech in Python, and change the language and pitch of the speech. You can further customize the speech by changing the text, language, and other parameters.



