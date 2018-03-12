#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
 
soil = 4
rain = 17
light = 18
sensor=Adafruit_DHT.DHT11
temp = 24
humidity, temperature = Adafruit_DHT.read_retry(sensor, temp)
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil, GPIO.IN)
GPIO.setup(rain, GPIO.IN)
GPIO.setup(light,GPIO.IN)
active_time = time.asctime()
 
def callback(soil):
        if GPIO.input(soil):
                print "Your plants are ok :)"
        else:
                print "Time to water the plants!" #Activate "must water" icon

GPIO.add_event_detect(soil, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soil, callback)

try: 

	if GPIO.input(rain):
		print ("Rain detected!") #Activate rainy icon | Deactivate "must water" icon
		print(tiempo + " It's raining.") #Log
    else:
    	print ("No rain detected.") #Deactivate rainy icon
    	print(tiempo + " It's not raining.") #Log

    if GPIO.input(light):
    	print ("Light detected.")
        print(tiempo + " It's sunny") #Log
    else:
    	print ("No light detected.")
        print(tiempo + " It's shady") #Log	

    if humidity is not None and temperature is not None:
 		print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperature, humidity))

	else:
  		print('Failed to get reading. Try again!')	

while True:
        time.sleep(1)