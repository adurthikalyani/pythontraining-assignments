num = int(input("Enter a number:"))
even = []
odd = []
if(num % 2 == 0):
	for i in range(num,num+10):
		if(i%2 == 0):
			even.append(i)
		else: 
			odd.append(i)
	print("Even Numbers:",even)
	print("Odd Numbers:",odd)
else:
	for i in range(num,num+10):
		if(i%2 == 0):
			even.append(i)
		else: 
			odd.append(i)
	print("Odd Numbers:",odd)
	print("Even Numbers:",even)