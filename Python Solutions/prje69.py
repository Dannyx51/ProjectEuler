from primeHelper import Prime
from time import time

st = time()

n = 1000; limit = 1000000

lp = Prime.genPrime(n,noBool = True)

res = 1
for i in lp: # look at the wikipedia definition for the totient function for this formula
    if res * i > limit: break
    res *= i
        
print(res)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 3E-4 seconds
