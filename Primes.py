# prime number calculator: find all primes up to n

max = int(input("Find primes up to what number? : "))
primeList = []
#for loop for checking each number
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
			
	if isPrime:
		primeList.append(x)
		
print(primeList)
		
		
#-------------------------------------------------------------
# prime number calculator: find the first n primes

i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i%j
        if a==0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1
