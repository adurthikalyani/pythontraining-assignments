size = int(input("size? : "))
col=int(input("col:"))

for i in range(size):
    for j in range(i*col, i*col+col):
        print(j+1, end=" ")
    print()