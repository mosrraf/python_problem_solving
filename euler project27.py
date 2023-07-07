from progress import progress 
def quad_eq():
	n=0
	counter=0
	arr=[]
	for a in range(-999,1000):
		counter+=1
		progress(counter,1998)
		for b in range(-999,1001):
			while isprime((n**2+a*n+b)):
				n+=1
			arr.append([a,b,n])
	return arr
def isprime(n):
	for i in range(2,int(abs(n)**0.5)):
		if n%i==0:
			return False
	return True
def max_primes(arr):
	primes=[arr[i][2] for i in range(0,len(arr()))]
	return arr()[primes.index(max(primes))]
arr=quad_eq()
print(max_primes(arr))
input()
