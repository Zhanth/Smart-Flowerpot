#!/usr/bin/python
import RPi.GPIO as GPIO
import time

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

try: 
	if GPIO.input(channel):
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

while True:
        time.sleep(1)