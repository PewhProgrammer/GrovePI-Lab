import time
import grovepi

# read prog args
if len(sys.argv) < 2:
  print('Usage: {} A<pin>'.format(sys.argv[0]))
  sys.exit(1)

air_sensor = int(sys.argv[1])

grovepi.pinMode(air_sensor,"INPUT")

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(air_sensor)

        if sensor_value > 700:
            print "High pollution"
        elif sensor_value > 300:
            print "Low pollution"
        else:
            print "Air fresh"

        print "sensor_value =", sensor_value
        time.sleep(.5)

    except IOError:
        print "Error"