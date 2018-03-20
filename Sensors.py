#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
soil = 4
light = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil, GPIO.IN)
GPIO.setup(light,GPIO.IN)
 
while True: 

    if GPIO.input(soil):
        soilStatus = 0

    else:
        soilStatus = 1

    if GPIO.input(light):
        lightStatus = 0

    else:
        lightStatus = 1

    if (soilStatus == 1 and lightStatus == 1):
        print("Your plants are ok.")

    if (soilStatus == 0 and lightStatus == 1):
        print("Your plants need more sunlight.")

    if (soilStatus == 1 and lightStatus == 0):
        print("Your plants need some water.")

    if (soilStatus == 0 and lightStatus == 0):
        print("Your plants need some water and more sunlight.")       

    time.sleep(1)