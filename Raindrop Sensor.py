# HIGH = no rain, LOW = rain detected

import time
import RPi.GPIO as GPIO
 
channel = GPIOx
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