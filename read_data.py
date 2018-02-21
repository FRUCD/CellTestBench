import time
import sys
import csv
import os
import threading as thr
import serial

CORRECTION_FACTOR = 2#1.80806

#listLock = thr.Lock()
'''
running = False

class io(thr.Thread):
    def __init__(self):
        thr.Thread.__init__(self)
    def run(self):
        while True:
            time.sleep(1)
            if not running:
                continue
            #listLock.acquire()
            print('Battery V: ' + str(resList[0]) + ' Resistor V: ' + str(resList[0]))
            #listLock.release()

listenThr = io()
listenThr.start()
'''
ser = serial.Serial('COM5', 9600, timeout=0)
print('Port acquired')

index = 0
resList = 2 * [0]

dataBuffer = ''
STATE = 0

fileNum = 0

while True:
    time.sleep(.1)
    try:
        data = ser.readline()
        if data == b'':
            continue
        data = data.decode('utf-8')
        dataBuffer += data
        i = dataBuffer.find('\n')
        if i != -1:
            data = dataBuffer[: i + 1 - len(os.linesep)]
            dataBuffer = dataBuffer[i + 1:]

        if STATE == 0:
            if data == 'START':
                STATE = 1
                try:
                    outputFile = open(str(fileNum) +'chargeData.csv', 'w', newline='')
                    print('Opened file')
                except:
                    print('File not opened')
                fileNum += 1
                out = csv.writer(outputFile)
                out.writerow(['voltage(V)', 'current(A)'])
                print("Started")
                #running = True
        elif STATE == 1:
            print(index)
            if data == 'DONE':
                index = 0
                dataBuffer = ''
                STATE = 0
                outputFile.close()
                #running = False
                print("Finished")

            else:
                resList[index % 2] = data

            if index % 2 == 1:
                row = [0, 0]
                valB = resList[0]
                valR = resList[1]
                bat_voltage = float(valB) #* .0049
                res_voltage = float(valR) * .0049
                current = (res_voltage - bat_voltage) * CORRECTION_FACTOR
                row[0] = bat_voltage * CORRECTION_FACTOR
                row[1] = (current) / .527778
                print(row)
                out.writerow(row)
            index += 1

    except:
        pass
