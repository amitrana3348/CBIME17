import urllib2
import time
import random
import RPi.GPIO as GPIO
import time,os
print "start"
none=""
response=none
DEBUG=1

GPIO.setmode(GPIO.BCM)

def RCtime (pin):
    reading=0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)

    while(GPIO.input(pin)==GPIO.LOW):
        reading+=1
    return reading
    #print "LDR=", reading

while True:
    print "While"
    print RCtime(4)
