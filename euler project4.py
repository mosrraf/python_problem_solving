def reverse(num):
	word=str(num)
	otherword=""
	for index in range(1,len(word)+1):
		otherword=otherword+word[-index]
	return(int(otherword))

	
value=int(input())
factors=sorted([num for num in range(10**(value-1),10**value)])
factors.reverse()
palindromes=[factor*other_factor for factor in factors for other_factor in factors if factor*other_factor==reverse(factor*other_factor)]
print(max(palindromes))					
