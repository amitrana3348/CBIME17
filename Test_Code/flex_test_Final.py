import RPi.GPIO as GPIO
import time


#in1 = 21   // Index    OK
#in2 = 20               Ok
#in3 = 16   // Pinky
#in4 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(16, GPIO.IN)

while True:

    in1 = GPIO.input(12)       # Pinky
    in2 = GPIO.input(16)       # Ring
    in3 = GPIO.input(20)       # Middle
    in4 = GPIO.input(21)       # Index
    
    if in4 == True and in3 == False and in2 == False and in1 == False:
        print("Index Finger")
        time.sleep(0.5)

    if in4 == False and in3 == True and in2 == False and in1 == False:
        print("Middle Finger")
        time.sleep(0.5)

    if in4 == False and in3 == False and in2 == True and in1 == False:
        print("Ring Finger")
        time.sleep(0.5)

    if in4 == False and in3 == False and in2 == False and in1 == True:
        print("Pinky Finger")
        time.sleep(0.5)

    if in4 == True and in3 == True and in2 == False and in1 == False:
        print("Index Finger & Middle Finger")
        time.sleep(0.5)

    if in4 == True and in3 == False and in2 == True and in1 == False:
        print("Index Finger & Ring Finger")
        time.sleep(0.5)

    if in4 == True and in3 == False and in2 == False and in1 == True:
        print("Index Finger & Pinky Finger")
        time.sleep(0.5)

    if in4 == True and in3 == True and in2 == True and in1 == False:
        print("Index & Middle & Ring Finger")
        time.sleep(0.5)

    if in4 == False and in3 == True and in2 == True and in1 == True:
        print("Middle & Ring & Pinky Finger")
        time.sleep(0.5)

    if in4 == True and in3 == True and in2 == True and in1 == True:
        print("Exit Mode")
        time.sleep(0.5)

    

    
    print("*****************")
    time.sleep(1)
    


        
