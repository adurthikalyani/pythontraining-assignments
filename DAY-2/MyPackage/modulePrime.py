def getPrime():
    __name__
prime_list=[]
start =int(input("enter start number: \t"))
for num in range(start,start+100):
	isPrime =True
	for i in range(2,num):
		if(num % i) == 0:
			isPrime =False
	if isPrime:
		prime_list.append(num)
print(prime_list)

if __name__ == "__main__":
    getPrime()