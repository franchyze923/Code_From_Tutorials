## I got this code from https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi

from gps import *
import time

running = True

def getPositionData(gps):
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        print "Your position: lon = " + str(longitude) + ", lat = " + str(latitude)

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    print "Application started!"
    while running:
        getPositionData(gpsd)
        time.sleep(1.0)

except (KeyboardInterrupt):
    running = False
    print "Applications closed!"