from primeHelper import Prime
from time import time

st = time()

n = 50000

def v1():
    primes = Prime.genPrime(n, noBool=True)

    l = {}
    for i in primes:
        x = i
        inc = 2
        while x <= n:
            if x not in l:
                l[x] = Prime.relativePrime(x,tot = True)

            x = i * inc
            inc += 1    
    return l

def v2():
    l = {}  
    for i in range(2,n+1):
        l[i] = Prime.relativePrime(i, tot = True)
    return l

st = time()
v1()
print(f"time taken for v1 : {time() - st}")

st = time()
v2()
print(f"time taken for v2 : {time() - st}")