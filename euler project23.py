#find number divisors
def num_divs(n):
	divs=[1]
	for num in range(2,int(n**0.5)+1):
		if n%num==0:
			divs.append(num)
			divs.append(int(n/num))
	return list(set(divs))
#find abundant numbers
def isabundant(n):
	if sum(num_divs(n))>n:
		return True
	return False
#list abundant numbers less than 28123
def abundant():
	abundants=[]
	for num in range(1,28112):#28123-12+1
		if isabundant(num):
			abundants.append(num)
	return abundants
#find numbers that are the sum of two abundant
def sum_2_abundants():
	ab_2=[]
	x=abundant()
	for i in range(0,len(x)):
		for j in range(i,len(x)):
			if x[i]+x[j]<28124:
				ab_2.append(x[i]+x[j])
	return list(set(ab_2))
#add all positive numbers till 28124 ignoring the sum of those numbers
print("sum of the positive numbers except the sum of 2 abundants: ",sum(num for num in range(1,28124))-sum(sum_2_abundants()))

