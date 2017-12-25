import urllib2
import time
import random
import RPi.GPIO as GPIO
import time
print "start"
none=""
response=none
GPIO.setmode(GPIO.BCM)
pin=4

while True:
    reading=0
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin,GPIO.IN)

    while(GPIO.input(pin)==GPIO.LOW):
        reading=reading+1

    
    print "LDR= ", reading


    
    myurl='https://thingspeak.com/update?key=0FD64HZOE4PJEEFJ&field1='+str(reading)
    print("sending HTTP request....")
    response=urllib2.urlopen(myurl)
    print"response code is=",response.code
    GPIO.cleanup()
    time.sleep(10)
    
