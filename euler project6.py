value=int(input())
#Easy solution:
#Sum=0
#squaresum=0
#for num in range(1,value+1):
#	Sum=Sum+num
#	squaresum=squaresum+num**2
#print(Sum**2-squaresum)


#mathematical solution: ex:(1+2+3)**2-(1**2+2**2+3**2)=2*(1*(1+1)+2*(2+1)) no formulas
#for num in range(1,value+1):
#	for othernum in range(num+1,value+1):
#		Sum=Sum+2*num*othernum
#print(Sum)


#mathematical solution in one line:
print(sum([2*num*othernum for num in range(1,value+1) for othernum in range(num+1,value+1)]))
