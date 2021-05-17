import time
from itertools import permutations
from primeHelper import genPrime

def checkdif(n):
  for i in range(len(n)-1):
    for j in range(1+i,len(n)):
      diff = n[j] - n[i]
      if n[j] + diff in n:
        return True
  return False

st = time.time()

lp = genPrime(10000,lowerBound = 1500)

for i in lp:
  p = list(permutations(str(i)))
  a = [int(''.join(c)) for c in p]
  a = list(set([m for m in a if m in lp]))
  a.sort()
  if len(a) >= 3:
    if checkdif(a):
      a = [str(x) for x in a]
      print(''.join(a))
      break

print("Time taken : " + str(time.time()-st))
#Avg Time Taken: 4E-3 seconds
