#first there are no one-digit number can be written as sum of digits to 5th power
#except 1 and it's not included
from time import time as T
def digit_fifth_power():
	Dig5=[i for i in range(1000,1000000) if sum(int(num)**5 for num in str(i))==i]
	return Dig5
start=T()
ans=digit_fifth_power()
print(sum(ans),ans,f"done in {T()-start} seconds") 
