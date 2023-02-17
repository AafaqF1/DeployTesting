import pygame
from gtts import gTTS
import pyttsx3
engin=pyttsx3.init()
pygame.mixer.init()
with open("READWhisper(Speech_To_Text).txt", "r") as f:
    text = f.read()
speech = gTTS(text)
engin.setProperty('pitch', -2.5)
engin.say(text)
engin.runAndWait()
speech.save("speech.mp3")
pygame.mixer.music.load("speech.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


