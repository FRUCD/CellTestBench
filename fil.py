from scipy import signal
import numpy as np
import csv

input = open('0chargeData.csv')
next(input)
reader = csv.reader(input)
data = list(reader)
data = [float(i[1]) for i in data]

oldStd = np.mean(data)

filtered = signal.medfilt(data)
print(len(filtered))
print(filtered)

newStd = np.mean(filtered)

print(oldStd)
print(newStd)