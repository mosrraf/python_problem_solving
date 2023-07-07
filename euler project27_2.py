from time import time
from calc import optimized_isprime as isprime

def equation(a,b):
    n=0
    while isprime(n**2+a*n+b):
        n+=1
    return n

def coeff_primes():
    primes=[equation(a,b)for a in range(-999,1000)for b in range(-1000,1001)]
    return primes

def max_primes():
    coeff=[[a,b] for a in range(-999,1000)for b in range(-1000,1001)]
    primes=coeff_primes()
    return coeff[primes.index(max(primes))]

if __name__ == '__main__':
    start = time()
    maximum=max_primes()
    print(maximum[0]*maximum[1])
    print(f"Execution time: {time()-start} seconds")
