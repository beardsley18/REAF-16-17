from vnpy import *
import time
import serial
s = VnSensor()
s.connect('COM4', 115200)

ser = serial.Serial('COM5', 9600)
time.sleep(2)

try:
    while True:
        ypr = s.read_yaw_pitch_roll()
        if(ypr.z > 25) and (ypr.z <90):
            ser.write('111'.encode('utf-8'))
        elif(ypr.z < -25) and (ypr.z >-90):
            ser.write('222'.encode('utf-8'))
        elif(ypr.z <= -90) or (ypr.z >= 90):
            ser.write('333'.encode('utf-8'))
        else:
            ser.write('000'.encode('utf-8'))
        ser.flush()
        abc = ser.read(5)   
        #print(abc.decode('utf-8'))
        print(abc)
        
        #time.sleep(1)

finally:
    ser.close()
