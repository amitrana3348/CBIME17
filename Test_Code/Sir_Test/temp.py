import urllib2
import time
import random
  
print "start"
none=""
response=none

while True:
    temp = random.randint (25,45)
    hum = random.randint (30,60)

    myurl = 'https://thingspeak.com/update?key=X9WO610SW1MKR1G3&field1='+str(temp)+'&field2='+str(hum)
    print ("sending HTTP request.....")
    response = urllib2.urlopen(myurl)
    print"response code is=",response.code
    time.sleep
