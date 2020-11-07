firstArray = [1, 2,-2,5,4 ,3,0]
firstArray.sort(reverse=False)
print(firstArray)

required = None
for num in range(firstArray[0],firstArray[-1]):
    if num not in firstArray:
        if num >0:
            required = num
if required == None:
    required = firstArray[-1]+1
    
print("Required:",required)
