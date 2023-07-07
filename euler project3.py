value=int(input())
b=True
primes=[]
for num in range(1,int(value**0.5)+1):
	if value%num==0:
		for div in range(2,int(num**0.5)):
			if num%div==0:
				b=False
				break 
		if b:
			primes.append(num)
print(max(primes))
