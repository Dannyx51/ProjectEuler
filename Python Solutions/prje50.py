from time import time
from primeHelper import Prime

st = time()

limit = 1000000
lp = Prime.genPrime(limit, noBool=True)

tlen = 0; find = 0; jl = len(lp)
for i in range(len(lp)):
    for j in range(i+tlen, jl):
        cur = sum(lp[i:j])
        
        if cur < limit:
            if cur in lp:
                tlen = j - i
                find = cur
        else:
            jl = j + 1
            break

print(find)
print(f"Time taken : {time() - st}")
#Avg Time Taken:  seconds