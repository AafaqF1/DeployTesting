from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
text = "Salut, je suis Aafaq Fazal et je travaille dans la société Datalytice, qui est la meilleure entreprise de science des données à Islamabad"
tts = gTTS(text, lang='fr',slow=False)
tts.save("hello French.mp3")
audio = AudioSegment.from_mp3("hello French.mp3")
audio.export("hello French.wav", format="wav")
audio = AudioSegment.from_wav("hello French.wav")
play(audio)