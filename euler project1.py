value=int(input())
print(sum(set([num for num in range(0,value,3)]+[num for num in range(0,value,5)])))
