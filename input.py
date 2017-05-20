from vnpy import *
import time
import serial
s = VnSensor()
s.connect('COM4', 115200)

while True:
	print(s.read_yaw_pitch_roll().z)
	time.sleep(.5)