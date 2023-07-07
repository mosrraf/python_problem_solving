def cycle_length(d):
  for i in range(1, d):
	  if 10**i % d == 1:
		  return i
  return 0


cycles = [[d,cycle_length(d)] for d in range(1, 1000)]
print(max(cycles[i][1] for i in range(0, 1000)))
