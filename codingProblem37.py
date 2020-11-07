initialSet = [1, 2, 3]
newSet = [[]]

for elem in initialSet:
    newSet.append([elem])


for i in range(0,len(initialSet)):
    while i != initialSet[i]:



print(newSet)