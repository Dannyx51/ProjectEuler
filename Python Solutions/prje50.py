from time import time
from primeHelper import Prime

st = time()

lp = Prime.genPrime(15, noBool=True)

ls = []; x = 0
for i in lp:
    x += i
    if x > 1000000: break
    ls.append(x)


# print(f"Time taken : {time() - st}")
#Avg Time Taken:  seconds