from __future__ import print_function
import serial,time
import NPi.GPIO as GPIO

try:
    input = raw_input
except NameError:
    pass
  
ser = serial.Serial('/dev/ttyS1',115200,timeout = 1)
#ser.open()

print(ser.portstr)

strInput = input("Enter some words:")
num = ser.write(strInput)
print(num)

time.sleep(1)
str = ser.read(num)#ser.readall()
print(str)
ser.close()

#try:
#    while True:
#        response = ser.readline()
#        print(response)
#except KeyboardInterrupt:
#    ser.close()

