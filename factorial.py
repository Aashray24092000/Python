def fact(n):
	if n < 0:
		return -1
	else:
		fact = 1
		for i in range(1, n+1):
			fact *= i
		return fact
print("input should be an integer")		
print(fact(5))
