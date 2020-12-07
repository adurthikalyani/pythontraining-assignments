def  factorial(number):
	if number== 1:
		return number
	else:
		return number*factorial(number-1)
number=int(input("enter number"))
print("factorial of",number,"is",factorial(number))