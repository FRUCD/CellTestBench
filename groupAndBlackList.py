import numpy as np
import pandas as pd

grouping = 3
target = 84
blacklist = [164, 169, 60, 102, 165, 136]

mistake = pd.read_csv("Data/mistake.csv")
for index, row in mistake.iterrows():
    if row['Group'] < 3:
        blacklist.append(int(row['Cell']))
        pass

table = pd.read_csv("Data/data.csv")
badIndices =  [index for index, row in table.iterrows() if int(row['Cell']) in blacklist]
print(badIndices)
table = table.drop(index=badIndices)
sort = table.sort_values("Diff", ascending=False)
topValues = sort[:target]
reverseTopValues = table.sort_values("Diff")
reverseTopValues = reverseTopValues[18:target+18]
average = sum(topValues['Diff']) / grouping
print(average)
groups = []
for i in range(grouping):
    groups.append([])

for i in range(target):
    group = pd.Series(data=int(i % grouping) + 3, index=["Group"])
    if int(i) % 2 is 0: 
        groups[i % grouping].append(topValues.iloc[i].append(group))
    else:
        groups[i % grouping].append(reverseTopValues.iloc[i - 1].append(group))

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
print("duplicates: ?")
print(frame.duplicated(subset="Cell"))
frame.duplicated(subset="Cell").to_csv("Data/duplicated.csv")
frame.to_csv("Data/grouped.csv", index=False)
justCells = frame.drop(columns=["OCV", "TailVolt", "Diff"])
justCells.to_csv("Data/checked.csv", index=False)
sort.to_csv("Data/sorted2.csv", index=False)