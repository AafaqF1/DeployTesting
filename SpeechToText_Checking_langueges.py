
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
text = "嘿，我 我在Datalytice公司工作，这是伊斯兰堡的顶级数据科学公司"
# English Language
# tts = gTTS(text, lang='en',slow=False)
# # France Language
# tts = gTTS(text, lang='fr',slow=False)
# # Spenish Language
# tts = gTTS(text, lang='es',slow=False)
# Chinese language
tts = gTTS(text, lang='zh-cn',slow=False)
audio = AudioSegment.from_mp3("hello Spenish.mp3")
audio.export("hello Spenish.wav", format="wav")
audio = AudioSegment.from_wav("hello Spenish.wav")
play(audio)