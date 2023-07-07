#!python3

PRIMENO = 10001

import itertools

oddprimes = [3]
currno = 2
for lo in itertools.count(5, 6):
    hi = lo + 2
    loprime = hiprime = True
    for prevprime in [p for p in oddprimes if p*p <= hi]:
        if lo % prevprime == 0:
            loprime = False
        if hi % prevprime == 0:
            hiprime = False
    if loprime:
        currno += 1
        print(currno, lo)
        if currno == PRIMENO:
            print(lo)
            break
        oddprimes.append(lo)
    if hiprime:
        currno += 1
        print(currno, hi)
        if currno == PRIMENO:
            print(hi)
            break
        oddprimes.append(hi)
