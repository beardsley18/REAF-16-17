import time
import serial

ser = serial.Serial('COM3', 9600)
time.sleep(2)

try:
    
    ser.write('G'.encode('utf-8'))
    ser.flush()
    abc = ser.read(1).decode('utf-8')
    while(abc[0] == 'Z'):
        ser.flush()
        print(abc)
        time.sleep(2)
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        

    ser.write('D'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
        
    ser.write('S'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    ser.flush()

except KeyboardInterrupt:
    pass

finally:
    ser.close()