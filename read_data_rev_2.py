import time
import sys
import csv
import os
import threading as thr
import win32com.client
import serial

connected = False
STATE = 0
fileNum = 0

#finds COM port that the Arduino is on (assumes only one Arduino is connected)
wmi = win32com.client.GetObject("winmgmts:")
for port in wmi.InstancesOf("Win32_SerialPort"):
    #print port.Name #port.DeviceID, port.Name
    if "Arduino" in port.Name:
        comPort = port.DeviceID
        print(comPort, "is Arduino")

#sets up serial connection (make sure baud rate is correct - matches Arduino)
ser = serial.Serial(comPort, 9600)

while not connected:
    serin = ser.read()
    connected = True

while True:
    #time.sleep(.1)
    try:
        data = ser.readline()
    except:
        print('Could not read data')
    #print(data)
    data = data.decode('utf-8')[:-2] # get rid of \r\n
    if STATE == 0:
        if data == 'START':
            STATE = 1
            try:
                fileName = str(fileNum) +'chargeData.csv'
                outputFile = open(fileName, 'w', newline='')
                print('Opened file: ' + fileName)
                fileNum += 1
            except:
                print('File not opened')
                continue
            out = csv.writer(outputFile)
            out.writerow(['voltage(V)', 'current(A)'])
            print("Started")
    elif STATE == 1:
        if data[0] == 'D':
            STATE = 0
            try:
                outputFile.close()
                print("Finished. File closed.")
            except:
                print('Finished. File NOT CLOSED')

        else:
            resList = [data.split()[i] for i in range(2)]
            resList[0] = float(resList[0]) * .0049 * 2
            print(resList)
            out.writerow(resList)
