from scipy import signal
import numpy as np
import csv

input = open('0chargeData.csv')
next(input)
reader = csv.reader(input)
data = list(reader)
data = [float(i[0]) for i in data]

oldStd = np.mean(data)

filtered = signal.wiener(data)
print(len(filtered))
print(filtered)

out = open('filterTest.csv', 'w')
for d in filtered:
    out.write(str(d) + '\n')

newStd = np.mean(filtered)

print(oldStd)
print(newStd)