def next_fibonacci(n_1,n_2):
	n=n_1+n_2
	return n
fibonacci=[1,1]
index=2
while len(str(fibonacci[index-1]))<1000:
	fibonacci.append(next_fibonacci(fibonacci[index-2],fibonacci[index-1]))
	index+=1
print(index)
