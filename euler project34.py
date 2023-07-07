def fact(n):
	if n<=1:
		return 1
	return n*fact(n-1)
def combinator(f,maximum_range):
	values=[]
	for i in range(10,maximum_range):
		sum=0
		for letter in str(i):
			sum+=f[int(letter)]
		if sum==i:
			values.append(i)
	return values
factorials=[fact(n)for n in range(0,10)]
print(sum(combinator(factorials,sum(factorials))))
