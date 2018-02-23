import re
import os
import shutil
START_INDEX = 101
digits = re.compile(r'(\d+)')
def tokenize(filename):
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))

def myKey(a):
    return tokenize(a)[1]


files = os.listdir()
files.sort(key=myKey)
print(files)
for f in files:
    shutil.move(f, '../../Data/' + str(START_INDEX) + tokenize(f)[2])
    START_INDEX += 1