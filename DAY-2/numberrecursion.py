def recursion(number):
	if number<=10:
		print(f'{number}',end= ' ')
		recursion(number+1)
		print(f'{number}',end= ' ')
recursion(1)
