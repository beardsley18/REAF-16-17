import time
import serial

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
time.sleep(2)

try:
    ser.write('a'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('S'.encode('utf-8')) #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
        
except KeyboardInterrupt:
    pass

finally:
    ser.close()