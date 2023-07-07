#the combination to form 2 pounds is calculated by:
#the general equation: A+2*B+5*C+10*D+20*E+50*F+100*G+200*H=200
#A domain(0,200)
#B domain(0,100)
#C domain(0,40)
#D domain(0,20)
#E domain(0,10)
#F domain(0,4)
#G domain(0,2)
#H domain(0,1)
def combinations():
	counter=0
	for H in range(0,2):
		for G in range (0,int((201-200*H)/100)+1):
			for F in range (0,int((201-100*G+200*H)/50)+1):
				for E in range (0,int((201-(50*F+100*G+200*H)/20))+1):
					for D in range (0,int((201-(20*E+50*F+100*G+200*H))/10)+1):
						for C in range (0,int((201-(10*D+20*E+50*F+100*G+200*H))/5)+1):
							for B in range (0,int((201-(5*C+10*D+20*E+50*F+100*G+200*H))/2)+1):
								for A in range (0,201-(2*B+5*C+10*D+20*E+50*F+100*G+200*H)+1):
									equation=A+2*B+5*C+10*D+20*E+50*F+100*G+200*H
									if equation==200:
										counter+=1
	return counter
print(combinations())
