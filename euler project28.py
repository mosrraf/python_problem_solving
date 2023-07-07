#generate a spiral numbers list(nxn):
#          . .........
#          . 7 8 9 10
#          . 6 1 2 11
#          . 5 4 3 12
#              ... 13
#we need corners so we start from center 
#there is a sequence there
#1,3,5,7,9,13,17,21,25,31,.....
#increments: 2,2,2,2,4,4,4,4,6,6,6,6,.....so on

def corners(n):
	corner=[1]
	num=2
	while corner[-1]<n**2:
		for rep in range(0,4):
			corner.append(corner[-1]+num)
		num+=2
	return corner
def isunicentered(corners,num):
	if corners[-1]==num**2:
		return sum(corner)
	return False
num=7
corner=corners(num)
print(isunicentered(corner,num))
