from primeHelper import Prime
from time import time

st = time()

s = 0
for i in range(1,1000000 + 1):
    s += Prime.totient(i)

print(s)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 36.1~ seconds