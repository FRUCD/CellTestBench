import time
import sys
import csv
import os
import threading as thr
import serial

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
                outputFile = open(str(fileNum) +'chargeData.csv', 'w', newline='')
                fileNum += 1
                out = csv.writer(outputFile)
                out.writerow(['battery', 'resistor'])
                print("Started")
                #running = True
        elif STATE == 1:
            if data == 'DONE':
                index = 0
                dataBuffer = ''
                STATE = 0
                outputFile.close()
                #running = False
                print("Finished")

            else:
                #listLock.acquire()
                resList[index % 2] = data
                #listLock.release()

            if index % 2 == 1:
                out.writerow(resList)

            index += 1

    except:
        pass
