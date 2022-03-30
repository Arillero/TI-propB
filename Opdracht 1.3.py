#Dit nooit uncommenten

import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO pulse" )

-----------

Om pulse te gebruiken # alles van tatatataaa.

def pulse( pin_nr, high_time, low_time):
   GPIO.output(pin_nr,GPIO.HIGH)
   time.sleep(high_time)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(low_time)

led = 18
GPIO.setup( led, GPIO.OUT )
while True:
   pulse( led, 0.2, 0.2 )

----------

Om tatatataaa te gebruiken # alles van pulse

def tatatataaa( pin_nr, high_time, low_time):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(low_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(low_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(low_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)

led = 18
GPIO.setup( led, GPIO.OUT )
while True:
   tatatataaa( led, 0.2, 0.2 )
