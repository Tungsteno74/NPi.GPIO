from __future__ import print_function
import NPi.GPIO as GPIO

ver_Bpi = GPIO.NPI_REVISION
ver_Gpio = GPIO.VERSION

print("BPi VERSION:\t\t",ver_Bpi)
print("NPi.GPIO VERSION:\t",ver_Gpio)
