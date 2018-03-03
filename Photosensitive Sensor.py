#!/usr/bin/python
import RPi.GPIO as GPIO
 
channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
 
for i in range(0,5):
    print GPIO.input(channel)