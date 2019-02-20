#!/usr/bin/env python
from __future__ import print_function
import NPi.GPIO as GPIO
import time
PIN_NUM = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)

GPIO.output(PIN_NUM,True)
print("\n value = %d\n" %(GPIO.input(PIN_NUM)))	
time.sleep(1)
GPIO.output(PIN_NUM,False)
print("\n value = %d\n" %(GPIO.input(PIN_NUM)))
time.sleep(1)

GPIO.cleanup()
