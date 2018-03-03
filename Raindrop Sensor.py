#link: http://raspi.tv/2017/make-a-rain-alert-system-with-raspberry-pi   
#
# raindrop sensor DO connected to GPIOx
# HIGH = no rain, LOW = rain detected
#import RPi.GPIO as GPIO
#
import time
from gpiozero import InputDevice
 
no_rain = InputDevice(x)
 
while True:
    if not no_rain.is_active:
        print("Rain detected!")
        # other code or functions
        # Log rainy days
        # Activate rainy icon on app
        # Deactivate "must water" icon on app
    time.sleep(1) 