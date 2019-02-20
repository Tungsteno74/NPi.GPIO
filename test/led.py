#!/usr/bin/env python
from __future__ import print_function
import NPi.GPIO as GPIO
import time
PIN_NUM = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)
while True:
    GPIO.output(PIN_NUM,True)
    time.sleep(1)
    GPIO.output(PIN_NUM,False)
    time.sleep(1)

