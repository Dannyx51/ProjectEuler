from primeHelper import Prime as p
from time import time

st = time()

lp = p.genPrime(100, lowerBound=2)

cur = 2
while True:
    l = [0 for i in range(5001)]
    l[0] = 1

    for i in range(len(lp)):
        for j in range(lp[i],cur+1):
            l[j] += l[j - lp[i]]

    if l[cur] > 5000: break
    cur += 1

print(cur)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 4E-2 seconds
