#/usr/bin/env python
import NPi.GPIO as GPIO
import time

try:
    input = raw_input
except NameError:
    pass

PIN_NUM = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)

p = GPIO.PWM(PIN_NUM,0.5)
p.start(50)

input("Press Enter to stop:")

p.stop()
GPIO.cleanup()
