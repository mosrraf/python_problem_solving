def get_text_list(txt_name):#transform text files into lists
	txt=open(txt_name+".txt").read()
	txt=txt[1:-2]
	names=txt.split('","')
	return names
def In(text):#input that only takes string
  bool=False
  while not bool:
    x=input(text)
    if x.isnumeric():
      print("Mistake, You should enter a string\n")
      bool=False
    else:
      bool=True
  return x
def existence(txt):#check if text file name exists and return it in a list
	bool=False
	while not bool:
		try:
			x=get_text_list(In(txt))
		except:
			print("your text file not existed,please try again\n")
			bool=False
			continue
		bool=True
	return x
def scores(names):#calculate score of each name and the total
	names.sort()
	alphapet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	score=[]
	total=0
	for i in range(0,len(names)):
		sum=0
		for j in range(0,len(names[i])):
			sum+=alphapet.index(names[i][j])+1
		sum*=i+1
		total+=sum
		score.append([names[i],sum])
	score.append(["Total",total])
	return score
print(scores(existence("please, enter text file name:"))[-1])
