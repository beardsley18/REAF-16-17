import time
import serial

ser = serial.Serial('COM3', 9600)
time.sleep(2)

command = ['FOR', 'UP*', 'DOW', 'RIG', 'LEF', 'HOV', 'BAC', 'RAN']
i = 0
try:
    while i<8:
        ser.write(command[i].encode('utf-8'))
        ser.flush()
        print('Sent command: ')
        print(command[i])
        arduinoFeedback = ser.read(3).decode('utf-8')
        print('Performing command: ')
        print(arduinoFeedback)
        time.sleep(2)
        i = i+1

except KeyboardInterrupt:
    pass

finally:
    ser.close()
