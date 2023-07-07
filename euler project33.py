# def cancelling(num,den):
	# num_w=str(num)
	# den_w=str(den)
	# for i in range(0,len(num_w)):
		# if num_w[i] in den_w and int(num_w[i])!=0:
			# if num_w!=den_w:
				# x,y="",""
				# for j in range(0,len(num_w)):
					# if num_w[j]!=num_w[i]:
						# x+=num_w[j]
				# for k in range(0,len(den_w)):	
					# if den_w[k]!=num_w[i]:
						# y+=den_w[k]
					# if (y!="" and x!=""):
						# if int(y)!=0:
							# if int(x)/int(y)==num/den:
								# return True
# def loop(num,den):
	# satisfy=[[n,d] for n in range(num,den) for d in range(n,den) if cancelling(n,d)]
	# return satisfy
# val=loop(10,100)
# mul_num=1
# mul_den=1
# for i in range(0,len(val)):
	# mul_num*=val[i][0]
	# mul_den*=val[i][1]
# print(int(mul_den/mul_num))

#ANOTHER WAY USING EQUATION
#(a*10+c)/(c*10+b)=a/b AT a!=0,b!=0,c!=0
def equation(a,b,c):
	if (a*10+c)/(c*10+b)==a/b:
		return b/a
values=[equation(a,b,c) for a in range(1,10)for c in range(a,10)for b in range (1,10) if equation(a,b,c)!=None]
mul=1
for value in values:
	mul*=value
print(int(mul))
			
