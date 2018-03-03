#!/usr/bin/python
import RPi.GPIO as GPIO
import time

channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

try:
	if GPIO.input(channel):
    	print ("Light detected.")
    	#Log sunlight time
    else:
    	print ("No light detected.")

while True:
        time.sleep(1)