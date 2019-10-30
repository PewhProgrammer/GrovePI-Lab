import sys
import time
import grovepi


# read prog args

if len(sys.argv) < 2:
  print('Usage: {} <pin>'.format(sys.argv[0]))
  sys.exit(1)

led_bar = sys.argv[1]
grovepi.pinMode(led_bar, "OUTPUT") # assign slot
grovepi.digitalWrite(led_bar,0.5)

## run loop

while (True):
  try:
    
    # grovepi.digitalWrite(led_bar,0.5)
    
    time.sleep(1)
  except IOError:
    print("Error")
