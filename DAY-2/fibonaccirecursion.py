def  fibonacci(number):
	if number<=1:
		return number
	else:
		return(fibonacci(number-1)+fibonacci(number-2))
numbers=int(input("enter number of terms"))
print("fibonacci series:")
for i in range(numbers):
	print(fibonacci(i))