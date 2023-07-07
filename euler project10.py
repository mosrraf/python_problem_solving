def isprime(value):
	if value==2:
		return True
	elif value==1:
		return False
	else:
		for num in range(2,int(value/2)+1):
			if value%num==0:
				break
		else:
			return True
		return False
value=int(input())
print(sum([prime for prime in range(1,value+1,2) if isprime(prime)]))
input()
