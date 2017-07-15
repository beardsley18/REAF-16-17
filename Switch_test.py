import time
import serial

ser = serial.Serial('COM3', 9600)
time.sleep(2)

ser.flush()
arduinoFeedback = ser.read(3).decode('utf-8')
print('Performing command: ')
print(arduinoFeedback)
