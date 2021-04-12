from primeHelper import Prime
from time import time

n = 10

st = time()
primes = Prime.genPrime(n, noBool=True)

l = {}
for i in primes:
    l[i] = i - 1
 
for i in range(4,n):
    if i not in l:
        divI = [int(i/x) for x in range(2,i) if i/x == int(i/x)]
        
        curT = 1
        

print(*l.items(), sep = '\n')