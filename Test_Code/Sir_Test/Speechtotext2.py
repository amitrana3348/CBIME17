#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import webbrowser
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index = 2, sample_rate = 48000) as source:
        audio = r.record(source, duration = 5)
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on People, I will show you where " + location + " is.")
        os.system("web-browser https://www.google.nl/maps/place/" + location )
    

# initialization
time.sleep(2)
speak("Hi People, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
