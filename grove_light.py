import time
import grovepi

light_sensor = 1

grovepi.pinMode(light_sensor, "INPUT")

while (True):
  try:
    print(grovepi.analogRead(light_sensor))
    time.sleep(1)
  except IOError:
    print("Error")
