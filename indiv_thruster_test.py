import time
import serial

ser = serial.Serial('COM3', 9600)
time.sleep(2)

try:
    ser.write('SV0'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('SM0'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('SDA'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('SDF'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('PV0'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('PM0'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('PDA'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('PDF'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('STO'.encode('utf-8')) #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(3).decode('utf-8')
    print(abc)
        
except KeyboardInterrupt:
    pass

finally:
    ser.close()