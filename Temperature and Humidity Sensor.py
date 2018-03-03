#https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/
import Adafruit_DHT

sensor=Adafruit_DHT.DHT11
gpio = 24
 
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
if humidity is not None and temperature is not None:
  print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperature, humidity))

else:
  print('Failed to get reading. Try again!')