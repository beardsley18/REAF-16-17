import time
import serial

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
time.sleep(2)

try:
    ser.write('F'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()
    
    ser.write('B'.encode('utf-8')) #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('U'.encode('utf-8')) #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('D'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('R'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('L'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('H'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('a'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
    abc = ser.read(1).decode('utf-8')
    print(abc)
    time.sleep(2)
    ser.flush()

    ser.write('b'.encode('utf-8'))  #change thruster each time
    ser.flush()
    # print('test')
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
    # print('test')
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