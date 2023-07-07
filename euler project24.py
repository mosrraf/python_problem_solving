def permutation(x,order):
	numbers=[str(num) for num in range(0,x)]
	permutation_n_1=[i+j for i in numbers for j in numbers if i!=j]
	for i in range(0,x-2):
		permutation_n=[i+j for i in numbers  for j in permutation_n_1 if i not in j]
		permutation_n_1=permutation_n
	return sorted(permutation_n)[order-1]
x=int(input("the maximum number you want in your permutations from 0 to 9: " ))
order=int(input("the order of permutation you want to get: "))
print(permutation(x+1,order))
