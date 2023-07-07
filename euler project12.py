value=int(input("Please, enter number of divisibles:"))
counter=1
triangular=counter
divisibles=0
print("" ,end='\n')
while divisibles<=value:
	counter+=1
	triangular+=counter
	divisibles=0
	for num in range(1,int(triangular**0.5)+1):
		if triangular%num==0:
			divisibles+=2
	print("Not Found Yet. Please, hang on for a moment, reached :",triangular,end="\r")
print("\rFound it",triangular,"Found after: ",counter,"tries"," with :", divisibles,"divisibles" )
input("press enter to close")
