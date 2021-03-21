import time
from math import *
from itertools import permutations

def checkdif(n):
  for i in range(len(n)-1):
    for j in range(1+i,len(n)):
      diff = n[j] - n[i]
      if n[j] + diff in n:
        return True
  return False


st = time.time()

n = 10000
prime = [True for i in range(n+1)] 
p = 2
while (p * p <= n): 
        
    # If prime[p] is not changed, then it is a prime 
    if (prime[p] == True): 
            
        # Update all multiples of p 
        for i in range(p * p, n+1, p): 
            prime[i] = False
    p += 1

lp = []
for i in range(1500,len(prime)-1):
    if prime[i]:
        lp.append(i)

del prime
#print(lp)
for i in lp:
  p = list(permutations(str(i)))
  a = [int(''.join(c)) for c in p]
  a = list(set([m for m in a if m in lp]))
  a.sort()
  if len(a) >= 3:
    if checkdif(a):
      print(a)
      break

print("Runtime: " + str(time.time()-st))
