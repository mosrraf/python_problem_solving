def d(n):
  #find the divisors of any number
  div=[]
  for num in range(1,int(n**0.5)):
    if n%num==0:
      div.append(num)
      if n/num!=n:
        div.append(int(n/num))
  #add the divisors
  return sum(div)
#finding amicable numbers to any range
def amc(n):
  amicable=[]
  for num in range(1,n+1):
    if d(d(num))==num and d(num)!=num:
      amicable.append(num)
      amicable.append(d(num))
  return set(amicable)
def In(text):
  bool=False
  while not bool:
    x=input(text)
    if not x.isnumeric():
      print("Mistake, You should enter a number\n")
      bool=False
    else:
      bool=True
  return int(x)
#subsitute
print("This application is used to calculate the sum of amicable numbers in certain range.")
x=In("Please, enter a number:")
print("amicable numbers in this range are: ",list(amc(x)),", and their sum is ",sum(amc(x)))
