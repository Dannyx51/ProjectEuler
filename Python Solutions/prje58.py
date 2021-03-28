from time import time
from primeHelper import Prime

st = time()

cur = 9
step = 2

numPrimes = 3
while (numPrimes/(2 * step + 1)) > 0.1:
    step += 2
    for i in range(3):
        cur += step
        if Prime.isPseudoPrime(cur): numPrimes += 1
    cur += step

print(step + 1)
print(f"Time taken : {time() - st}")
#Avg Time Taken: ~0.3 seconds