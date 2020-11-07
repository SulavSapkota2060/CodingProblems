initialList = [1,2,3,4,5]

newList = []

for i in initialList:
    product =1
    for j in initialList:
        if j!=i:
            product = product*j
    newList.append(product)


print(newList)
        