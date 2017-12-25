import time
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

import RPi.GPIO as GPIO,time,os
GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD()
lcd.begin(16, 2)

lcd.clear()

while True:
    lcd.setCursor(0,0)
    lcd.message("Hello World")
    time.sleep(2)
    lcd.clear()
    lcd.setCursor(0,1)
    lcd.message("Hello World !!!!!")
    time.sleep(2)
    lcd.clear()

      
