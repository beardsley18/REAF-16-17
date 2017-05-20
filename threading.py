import _thread
import time
import serial

ser = serial.Serial('COM5', 9600)

def read_in(threadName):
    while True:
        print('read %s'%(ser.readline().decode('utf-8')))

def write_out(threadName):
    for count in range(10):
        ser.write(str(count).encode('utf-8'))
        print('write %s'%count)
        time.sleep(1)
        #ser.flush()
    
try:
   _thread.start_new_thread( read_in, ("Thread-1",) )
   _thread.start_new_thread( write_out, ("Thread-2",) )
except:
   print("Error: unable to start thread")
   
while True:
    pass