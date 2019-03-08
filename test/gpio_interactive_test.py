#!/usr/bin/env python
from __future__ import print_function
import sys
try:
    import NPi.GPIO as GPIO
except RuntimeError:
    print("Error importing GPIO modules! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
    sys.exit(-1)  
import time

try:
    input = raw_input
except NameError:
    pass

print("Inizializing...\n")
range_pins = [3,24] #range of board GPIO pins to check
inv_pins = [4,6,9,14,17,20] #pins that aren't onboard GPIOs
v_modes_str = ["LOW","HIGH"]


GPIO.setmode(GPIO.BOARD)

time.sleep(0.2)

#print "Board revision:"
#print GPIO.RPI_INFO
#print GPIO.RPI_REVISION
print("\nNPi.GPIO version:")
print(GPIO.VERSION)

time.sleep(1)
           
while True:
    try:
        pin = int(input('Choose board pin number: \n( 3 - 24; excluded: 4, 6, 9, 14, 17, 20 )\n'))
        mode = int(input('Choose pin state: \n( 0 - Low, 1 - High, 2 - Quit )\n'))
        print("\n\nChoosen %d (state %s)\n" % (mode, v_modes_str[mode]))
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, mode)
        time.sleep(0.5)
        print("Pin state changed!\n")
        #GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        time.sleep(0.5)
        print("Now pin %d state is: %s\n" % (pin, v_modes_str[GPIO.input(pin)]))    
        time.sleep(3)
    except ValueError:
        print("Not a number")
        continue
    except IndexError:
        if mode == 2:
            GPIO.cleanup()
            print("Bye :-(\n")
            break
        print("Not a valid pin or mode")
        continue
