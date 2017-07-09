#from vnpy import *
import time
import serial
#s = VnSensor()
#s.connect('COM4', 115200)

ser = serial.Serial('COM3', 9600)
time.sleep(2)

#while True:
#ypr = s.read_yaw_pitch_roll()
#if(ypr.z > 25):
 #   ser.write(1)
#else:
#    ser.write(0)
try:
    while True:
        #ypr = s.read_yaw_pitch_roll()
        #ser.write(('%s'%ypr.z).encode('utf-8')) #converts float to string to byte
        ser.write('FOR'.encode('utf-8'))
        #print(('%s'%ypr.z).encode('utf-8'))
        ser.flush()
        #print(ypr.z)
        print('test')
        #time.sleep(1)
        abc = ser.read(3).decode('utf-8')
        print(abc)
        time.sleep(2)

        
except KeyboardInterrupt:
    pass

finally:
    ser.close()
#master - get bootstrap from Arduino first
    #read, pass in size (don't use readline)
