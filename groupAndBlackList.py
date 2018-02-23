import numpy as np
import pandas as pd

grouping = 6
target = 60
blacklist = [164, 169, 60, 102, 165]

table = pd.read_csv("Data/diffs.csv")
sort = table.sort_values("Diff", ascending=False)
badIndices =  [index for index, row in sort.iterrows() if row['Cell'] in blacklist]
sort.drop(index=badIndices)
topValues = sort[:target]
reverseTopValues = topValues.sort_values("Diff")
print(topValues)
average = sum(topValues['Diff']) / grouping
print(average)
groups = []
for i in range(grouping):
    groups.append([])

for i in range(target):
    group = pd.Series(data=int(i % grouping), index=["Group"])
    if int(i/grouping) % 2 is 0: 
        groups[i % grouping].append(topValues.iloc[i].append(group))
    else:
        groups[i % grouping].append(reverseTopValues.iloc[i].append(group))

for i in range(grouping):
    print("average: " + str(i))
    diff = [row['Diff'] for row in groups[i]]
    print(sum(diff)/len(diff))
    print("length: " + str(len(groups[i])))
    for j in range(len(groups[i])):
        frame_i = groups[i][j].to_frame().transpose()
        frame_i[['Group', 'Cell']] = frame_i[['Group', 'Cell']].astype(int)
        groups[i][j] = frame_i
    groups[i] = pd.concat(groups[i], ignore_index=True)

frame = pd.concat(groups, ignore_index=True)
print(frame)
frame.to_csv("Data/grouped.csv", index=False)
sort.to_csv("Data/sorted.csv", index=False)