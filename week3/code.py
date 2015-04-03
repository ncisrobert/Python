import time, serial
ser = serial.Serial("COM6",9600,timeout=2)

while(True):
    ser.write("1")
