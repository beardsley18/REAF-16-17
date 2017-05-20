from vnpy import *
import time
import serial
s = VnSensor()

ser = serial.Serial('COM5', 9600)
print(ser.is_open)
print(ser.readline())
print('writing')
ser.write(b'\x01\x02'*100)
print(ser.out_waiting)
ser.flush()
print(ser.out_waiting)
abc = ser.read(size=3)
print(abc)

