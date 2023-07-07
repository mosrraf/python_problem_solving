from time import time
value=int(input())
b=True
counter=0
mul=1
start = time()
for num in range(0,int(value/5)):
	mul*=value-num
while b:
	counter+=mul
	for num in range(1,value+1):
		if counter%num==0:
			b=False
		else:
			b=True
			break
print(counter,str((time()-start)*10**3)+" ms")
