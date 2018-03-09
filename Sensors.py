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
 
def callback(soil):
        if GPIO.input(soil):
                print "Your plants are ok :)"
        else:
                print "Time to water the plants!"
                # Activate "must water" icon on app

GPIO.add_event_detect(soil, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soil, callback)

try: 

	if GPIO.input(rain):
		active_time = time.time()
		print ("Rain detected!")
		print (active_time)
		# other code or functions
        # Log rainy days
        # Activate rainy icon on app
        # Deactivate "must water" icon on app
    else:
    	print ("No rain detected.")
    	print (active_time)

    if GPIO.input(light):
    	print ("Light detected.")
    	#Log sunlight time
    else:
    	print ("No light detected.")	

    if humidity is not None and temperature is not None:
 		print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperature, humidity))

	else:
  		print('Failed to get reading. Try again!')	

while True:
        time.sleep(1)