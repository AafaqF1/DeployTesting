from gtts import gTTS
import pygame
from langdetect import detect
text = "你好，这是一个文本转语音的示例"
tts = gTTS(text, lang='zh-cn')
tts.save("helloChina.mp3")
pygame.init()
pygame.mixer.music.load("helloChina.mp3")
pygame.mixer.music.play()
pygame.event.wait()