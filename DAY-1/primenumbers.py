num = 100
c = int(input("Enter the number: "))
while num != 0:
	for i in range(2,c):
		if c%i == 0:
			break
	else:
		print(c)
		num -= 1
	c+=1