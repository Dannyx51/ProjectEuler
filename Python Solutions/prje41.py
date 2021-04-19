from itertools import permutations
from functools import reduce
from time import time
from primeHelper import Prime

st = time()

l = [int(reduce(lambda x,y: x + y, p)) for p in list(permutations("1234567"))]

lp = Prime.genPrime(7654321,lowerBound = 7123456)

lpan = []  
for i in l:
    gaming = False
    for ii in lp:
        if i % ii == 0:
                gaming = True
                break
    if gaming:
        lpan.append(i)   

print(max(lpan))
print(f"Time taken : {time() - st}")
# Avg Time Taken: 15.3 seconds