import serial
import matplotlib.pyplot as plt
import numpy as np
import win32com.client

connected = False

#finds COM port that the Arduino is on (assumes only one Arduino is connected)
wmi = win32com.client.GetObject("winmgmts:")
for port in wmi.InstancesOf("Win32_SerialPort"):
    #print port.Name #port.DeviceID, port.Name
    if "Arduino" in port.Name:
        comPort = port.DeviceID
        print(comPort, "is Arduino")

ser = serial.Serial(comPort, 9600) #sets up serial connection (make sure baud rate is correct - matches Arduino)

while not connected:
    serin = ser.read()
    connected = True

for i in range(10):
    data = ser.readline()
    print(data)
