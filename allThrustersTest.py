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
        

    ser.write('a'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('b'.encode('utf-8'))  #change thruster each time
    ser.flush()
    print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('c'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('d'.encode('utf-8'))  #change thruster each time
    ser.flush()
    print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('e'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('f'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('g'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('h'.encode('utf-8'))  #change thruster each time
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
    time.sleep(2)
    ser.flush()

except KeyboardInterrupt:
    pass

finally:
    ser.close()