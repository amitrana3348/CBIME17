import time
import pyttsx

def tts(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()

tts('hello world')
