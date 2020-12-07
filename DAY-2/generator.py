myList = [
    [1001, 'ABC', 1000.00, 'f'],
    [1002, 'XYZ', 1450.59, 'm'],
    [1003, 'PQR', 2398.99, 'f'],
    [1004, 'LMN', 2985.00 , 'f']
]

l = len(myList)
for i in range(l):
    for j in range(3):
        if(myList[j][0] > myList[j+1][0]):
            myList[j][0], myList[j+1][0] = myList[j+1][0], myList[j][0]
for i in range(l):
    if(myList[i][3] == 'm'):
        myList[i][1] = 'Mr.' + myList[i][1]
    elif(myList[i][3] == 'f'):
        myList[i][1] = 'Ms.' + myList[i][1]
    myList[i][2] = myList[i][2] + (myList[i][2] * 0.1)
print(myList)

