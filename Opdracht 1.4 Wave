import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def pulse( pin, delay1, delay2 ):
   while True:
      GPIO.output(pin, GPIO.HIGH)
      time.sleep(delay1)
      GPIO.output(pin, GPIO.LOW)
      time.sleep(delay2)

def servo_pulse( pin_nr, position ):
   hightime = 0.00002*position+0.0005
   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(hightime)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(0.02 - hightime)


servo = 17
GPIO.setup( servo, GPIO.OUT )
while True:
   for i in range( 0, 100, 1 ):
      servo_pulse( servo, i )
   time.sleep(0.5)
   for i in range( 100, 0, -1 ):
      servo_pulse( servo, i )
   time.sleep(0.5)
