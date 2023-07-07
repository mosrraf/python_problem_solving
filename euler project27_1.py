from time import time
from math import sqrt


# pythran export is_prime(int)
def is_prime(x):
    """Return true if n is prime."""
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


# pythran export formula(int, int, int)
def formula(a, b, n):
    return (n * n) + (a * n) + b


# pythran export count_primes(int, int)
def count_primes(a, b):
    counter = 0

    while True:
        result = formula(a, b, counter)
        if is_prime(result):
            counter += 1
        else:
            return counter


# pythran export main()
def main():
    result = (0, 0, 0)

    for a in range(1000, -1000, -1):
        for b in range(1000, 0, -1):
            r = count_primes(a, b)
            if r > result[2]:
                result = (a, b, r)
    print(result)
    print(result[0] * result[1])
start=time()
main()
print(time()-start)
