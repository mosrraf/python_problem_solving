from time import time
value=int(input())
primes=[2]
counter=1
start=time()
while len(primes)<value:
	counter+=2
	for num in primes:
		if counter%num==0:
			b=False
			break
		else:
			b=True
	if b:
		primes.append(counter)	
End=time()
print(primes[value-1]," ",End-start," secs")
