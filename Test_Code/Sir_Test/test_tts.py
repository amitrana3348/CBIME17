import time
import pyttsx
engine = pyttsx.init()
engine.say('Good morning. this is raspberry pi speaking')
engine.runAndWait()

from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
