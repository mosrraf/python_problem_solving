value=int(input())
Fibonacci=[1,2]
num=0
while Fibonacci[-1]<value:
	num=num+1
	Fibonacci.append(Fibonacci[num]+Fibonacci[num-1])	
print([Fibonacci[n] for n in range(0,len(Fibonacci)) if Fibonacci[n]%2==0 ],sum([Fibonacci[n] for n in range(0,len(Fibonacci)) if Fibonacci[n]%2==0 ]))
