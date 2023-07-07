def distinct_numbers():
	numbers=[a**b for a in range(2,101) for b in range(2,101)]
	numbers=list(set(numbers))
	return numbers
print(len(distinct_numbers()))
