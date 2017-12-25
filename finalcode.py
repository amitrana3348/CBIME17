import sys
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import speech_recognition as sr
import time
import pyttsx
import warnings


import RPi.GPIO as GPIO,time,os

GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD()
lcd.begin(16, 2)

GPIO.setup(21, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(16, GPIO.IN)

lcd.clear()

my_recognized_audio = "Nothing Said"

def tts(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()

print '*** MultiCommunication System For physically disabled people using raspberry pi ***'
print " "

tts('MultiCommunication System For physically disabled people using raspberry pi')

while True:
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.message("Select Mode :")
    print " "
    print " * Select Mode *"
    print " "
    print "Mode1 : Keyboard Mode"
    print "Mode2 : Speech to Text Mode"
    print "Mode3 : Gesture Mode"
    print " "
    time.sleep(1)
    tts('Select Mode')
    
    lcd.setCursor(0,1)
    lcd.message("1.K 2.S to T 3.G")
    
    selection = raw_input('Select Mode :  ')
    
    if selection == '1':
        time.sleep(0.5)
        tts('Keyboard Mode Selected')
        print 'Keyboard Mode Selected'
        lcd.setCursor(0,0)
        lcd.message("Select Mode :")
        lcd.setCursor(13,0)
        lcd.message("1")
        lcd.setCursor(0,1)
        lcd.message("Keyboard Mode Selected")
        time.sleep(2)
        
        while True:
            lcd.clear()
            lcd.setCursor(0,0)
            lcd.message("*Keyboard Mode*")
            lcd.setCursor(0,1)
            lcd.message("Press Key :")
            print ' '
            selection = raw_input('Press Key : ')

            if selection == '0':
                print 'Keyboard Mode Exit'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Key Mode Exit")
                tts('Keyboard Mode Exit')
                time.sleep(2)
                break
            
            if selection == 'T' or selection == 't':
                print 'I Want to go Toilet'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Want to go Toilet")
                tts('I want to go toilet')
                time.sleep(2)
                lcd.clear()

            if selection == 'W' or selection == 'w':
                print 'I Want Water'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("I Want Water")
                tts('I Want Water')
                time.sleep(2)
                lcd.clear()

            if selection == 'F' or selection == 'f':
                print 'I Want Food'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("I Want Food")
                tts('I Want Food')
                time.sleep(2)
                lcd.clear()

            if selection == 'M' or selection == 'm':
                print 'I need Mobile'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("I need Mobile")
                tts('I need Mobile')
                time.sleep(2)
                lcd.clear()

            if selection == 'O' or selection == 'o':
                print 'I Want to go out'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Want to go out")
                tts('I Want to go out')
                time.sleep(2)
                lcd.clear()

            if selection == 'B' or selection == 'b':
                print 'I Want to take bath'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Want to take bath")
                tts('I Want to take bath')
                time.sleep(2)
                lcd.clear()

            if selection == 'C' or selection == 'c':
                print 'I Want to change cloths'
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Change Cloths")
                tts('I Want to change Cloths')
                time.sleep(2)
                lcd.clear()

            
                
    elif selection == '2':
        time.sleep(0.5)
        lcd.clear()
        tts('Speech to text Mode Selected')
        print 'Speech to text Selected'
        lcd.setCursor(0,0)
        lcd.message("Select Mode :")
        lcd.setCursor(13,0)
        lcd.message("2")
        lcd.setCursor(0,1)
        lcd.message("Speech to Text")
        time.sleep(2)
        lcd.clear()

        while True:
            #lcd.clear()
            r = sr.Recognizer()
            with sr.Microphone(device_index = 2, sample_rate = 48000) as source:
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Say Something: ")
                print "say something Now\n"
                audio = r.record(source, duration = 5)
                print "recording Done\n"
                lcd.clear()
                lcd.setCursor(0,0)
                lcd.message("Recording Done: ")
            with open("microphone-results.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:
                my_recognized_audio = r.recognize_google(audio)
                print " "
                print("You said: " + my_recognized_audio)
                print " "
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                print " "
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                print " "
            
            lcd.clear()
            lcd.setCursor(0,0)
            lcd.message("You Say : ")
            lcd.setCursor(0,1)
            lcd.message(my_recognized_audio) 
            time.sleep(2)
            if my_recognized_audio == 'EXIT' or my_recognized_audio == 'Exit' or my_recognized_audio == 'exit':
                print " Speech to Text Mode Exit"
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Mode Exit")
                tts('Speech to Text Mode Exit')
                break


    elif selection == '3':
        time.sleep(0.5)
        lcd.clear()
        tts('Gesture Mode Selected')
        print 'Gesture Mode Selected'
        lcd.setCursor(0,0)
        lcd.message("Select Mode :")
        lcd.setCursor(13,0)
        lcd.message("3")
        lcd.setCursor(0,1)
        lcd.message("Gesture Mode")
        time.sleep(2)

        while True:
            in1 = GPIO.input(12)       # Pinky
            in2 = GPIO.input(16)       # Ring
            in3 = GPIO.input(20)       # Middle
            in4 = GPIO.input(21)       # Index
            
            lcd.setCursor(0,0)
            lcd.message("Give Motion :")

            if in4 == True and in3 == False and in2 == False and in1 == False:
                print("I Want to go Toilet")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Want to go Toilet :")
                time.sleep(0.5)

            if in4 == False and in3 == True and in2 == False and in1 == False:
                print("I Want Water")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("I Want Water")
                time.sleep(0.5)

            if in4 == False and in3 == False and in2 == True and in1 == False:
                print("I Want Food")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("I Want Food")
                time.sleep(0.5)

            if in4 == False and in3 == False and in2 == False and in1 == True:
                print("I need Mobile")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("I need Mobile")
                time.sleep(0.5)
                
            if in4 == True and in3 == True and in2 == False and in1 == False:
                print("I Want to go out")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Want to Go out")
                time.sleep(0.5)

            if in4 == True and in3 == False and in2 == True and in1 == False:
                print("I Want to take bath")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Want to take bath")
                time.sleep(0.5)

            if in4 == True and in3 == False and in2 == False and in1 == True:
                print("I Want to change cloths")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Change Clothes")
                time.sleep(0.5)

            if in4 == True and in3 == True and in2 == True and in1 == False:
                print("Play Music")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Play Music")
                time.sleep(0.5)

            if in4 == False and in3 == True and in2 == True and in1 == True:
                print("I Want Tea")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("I Want Tea")
                time.sleep(0.5)

            if in4 == True and in3 == True and in2 == True and in1 == True:
                print("Exit Mode")
                lcd.clear()
                lcd.setCursor(0,1)
                lcd.message("Mode Exit")
                tts('Gesture Mode Exit')
                time.sleep(0.5)
                break

            
        
    else:
        print 'Wrong Mode'
        lcd.setCursor(0,1)
        lcd.message("Wrong Mode")
        time.sleep(2)
