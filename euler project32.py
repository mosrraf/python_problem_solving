#to find pan_digital 1 through 9 we have several probabilities:
#if 1-digit number x 4-digit number=4-digit number
#if 2-digit number x 3-digit number=4-digit number
#in first condition 1 is ignored cause ever thing x 1 is the same
def pan_digital_1_9():
	numbers_1_digit=[i for i in range(2,10)]
	numbers_2_digit=[i for i in range(10,99)]
	numbers_3_digit=[i for i in range(100,999)]
	numbers_4_digit=[i for i in range(1000,9999)]
	string_pan=[str(i) for i in range(1,10)]
	#our preparations is done, now let's go into the surgery
	pan_9=[]
	for num1 in numbers_1_digit:
		for num2 in numbers_4_digit:
			muln=num1*num2
			mulw=str(num1*num2)
			if len(mulw)==4:
				word=sorted(str(num1)+str(num2)+mulw)
				if word==string_pan:
					if not muln in pan_9:
						pan_9.append(muln)
	for num1 in numbers_2_digit:
		for num2 in numbers_3_digit:
			muln=num1*num2
			mulw=str(num1*num2)
			if len(mulw)==4:
				word=sorted(str(num1)+str(num2)+mulw)
				if word==string_pan:
					if not muln in pan_9:
						pan_9.append(muln)
	return pan_9
array=pan_digital_1_9()
print(array,sum(array))
