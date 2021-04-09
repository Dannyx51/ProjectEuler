from primeHelper import Prime
from time import time

st = time()
n = 1000000 #im hoping that this has the set im looking for in it

prime = Prime.genPrime(n) 

l = []
for i in range(10,len(prime)):
  gaming = True
  t = str(i)
  for j in range(len(t)):
    gaming = prime[int(t[j:])]
    if not gaming: break
  if not gaming: continue
  for j in range(1,len(t)):
    gaming = prime[int(t[:j])]
    if not gaming: break
  if not gaming: continue
  l.append(i)

print(sum(l))
print(f"Time taken : {time() - st}")
#Avg Time Taken: ~1 second