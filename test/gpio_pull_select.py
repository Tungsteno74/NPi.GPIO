#!/usr/bin/env python
import sys
try:
    try:
        import NPi.GPIO as GPIO
    except ImportError:
        try:
            import RPi.GPIO as GPIO
        except ImportError:
            print("Failed to import GPIO modules! You need NPi.GPIO or RPi.GPIO")
            sys.exit(-1)
except RuntimeError:
    print("Error importing GPIO modules! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
    sys.exit(-1)
import time

range_pins = [3,24] #range of GPIO pins to check
inv_pins = [4,6,9,14,17,20] #pins that aren't onboard GPIOs
v_modes = [GPIO.PUD_DOWN,GPIO.PUD_UP,GPIO.PUD_OFF] #Pull's states
v_modes_str = ["Down","Up","Off"]

GPIO.setmode(GPIO.BOARD)

def modetype(mode):
    for pin in xrange(range_pins[0],range_pins[1] + 1):
        if not pin in inv_pins: 
            GPIO.setup(pin, GPIO.IN, pull_up_down = mode)
            print "value_%d = %d" % (pin,GPIO.input(pin)) 
            time.sleep(0.1)

while True:
    try:
        modenum = int(raw_input('Choose resistor pull modes: \n( 0 - Active Pull Down, 1 - Active Pull Up, 2 - Disable Pull, 3 - Quit )\n'))
        print "\n\nChoosen %d (Pull %s)\n" % (modenum, v_modes_str[modenum])
        time.sleep(2)
        modetype(v_modes[modenum])
        print "Pins Pull %s ends\n" % (v_modes_str[modenum])
        time.sleep(3)
    except ValueError:
        print "Not a number"
        continue
    except IndexError:
        if modenum == 3:
            #GPIO.cleanup
            print "Bye :-(\n"
            break
        print "Not a valid mode"
        continue