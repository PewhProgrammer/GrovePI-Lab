import time
import grovepi

sensor = 3

grovepi.pinMode(sensor, "INPUT")

while True:
  try:
    x = grovepi.digitalRead(sensor)
    if x == 1:
      print("black detected")
    else:
      print("white detected >> " +  str(x) )
    time.sleep(1)
  except IOError:
    print("Error")
