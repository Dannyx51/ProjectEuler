from primeHelper import Prime
from time import time

st = time()

n = 10
primes = Prime.genPrime(n, noBool=True)

l = {}
for i in primes:
    x = i
    while x < n:
        pass

print(l)