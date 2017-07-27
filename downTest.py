import time
import serial
from datetime import datetime

ser = serial.Serial('COM3', 9600)
time.sleep(2)

curr_time = datetime.now()
with open('output_'+str(curr_time.hour)+str(curr_time.minute)+str(curr_time.second)+'.txt', 'w') as outFile:

    while True:
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        ser.flush()
        while(abc[0] == 'Z'):
            print(abc)
            time.sleep(.2)
            ser.write('G'.encode('utf-8'))
            ser.flush()
            abc = ser.read(1).decode('utf-8')
            outFile.write(abc)
            outFile.write('\n')
            ser.flush()
      
            
        ser.write('N'.encode('utf-8'))  
        ser.flush()
        # print('test')
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        print(abc)
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        while(abc[0] == 'G'):
            ser.flush()
            print(abc)
            time.sleep(.2)
            ser.write('G'.encode('utf-8'))
            outFile.write(abc)
            outFile.write('\n')
            ser.flush()
            abc = ser.read(1).decode('utf-8')
            outFile.write(abc)
            outFile.write('\n')
            ser.flush()
        
            
            
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        while(abc[0] == 'Z'):
            ser.flush()
            print(abc)
            time.sleep(.2)
            ser.write('G'.encode('utf-8'))
            ser.flush()
            abc = ser.read(1).decode('utf-8')
            outFile.write(abc)
            outFile.write('\n')
            
        
        ser.write('F'.encode('utf-8'))  #change thruster each time
        ser.flush()
        # print('test')
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        print(abc)
        ser.flush()
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        while(abc[0] == 'G'):
            ser.flush()
            print(abc)
            time.sleep(.2)
            ser.write('G'.encode('utf-8'))
            ser.flush()
            abc = ser.read(1).decode('utf-8')
            outFile.write(abc)
            outFile.write('\n')
            ser.flush()
        
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        ser.flush()
        while(abc[0] == 'Z'):
            print(abc)
            time.sleep(.2)
            ser.write('G'.encode('utf-8'))
            ser.flush()
            abc = ser.read(1).decode('utf-8')
            outFile.write(abc)
            outFile.write('\n')
            ser.flush()
            
        
        ser.write('D'.encode('utf-8'))  #change thruster each time
        ser.flush()
        # print('test')
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        print(abc)
        ser.flush()
        ser.write('G'.encode('utf-8'))
        ser.flush()
        abc = ser.read(1).decode('utf-8')
        outFile.write(abc)
        outFile.write('\n')
        ser.flush()
        while(abc[0] == 'G'):
            print(abc)
            time.sleep(.2)
            ser.write('G'.encode('utf-8'))
            ser.flush()
            abc = ser.read(1).decode('utf-8')
            outFile.write(abc)
            outFile.write('\n')
            ser.flush()
        
ser.close()