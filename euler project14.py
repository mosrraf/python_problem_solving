from time import time
def indexfinder(value,container):
	for num in range(0,len(container)):
		if value==container[num]:
			return num
counter=0
number=1
chain=[]
while number<1000000:
	start=time()
	number+=1
	counter=0
	num=number
	while num!=1:
		if num%2==0:
			num/=2
		else:
			num=3*num+1
		counter+=1
	chain.append(counter)
	print("The calculation may take a while, progress:", number/10000,"% ",end="\r")
print("the value under 1000000 with longest chain is:",indexfinder(max(chain),chain)+2," with chain length:",max(chain)," time taken:",(time()-start)*1000,"secs")	
input()
