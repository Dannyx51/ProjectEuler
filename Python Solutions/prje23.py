import time
from math import *
def d(n):
  s = 1
  st = sqrt(n)
  for i in range(2,int(st)+1):
      if n % i == 0:
        s += i + n / i
  if int(st) == st:
    s -= st
  return s

s = time.time()
#create set of [ab]undant numbers
#sets are just stupid fast for searches, slower if iterating
ab = set()
limit = 20162
total = 0
for i in range(1, limit):
  #print(i)
  if d(i) > i:
    ab.add(i)
  #is i - number = another abundant number?
  if not any((i - n in ab) for n in ab):
    total += i


#print(total)
print("Runtime: " + str(time.time()-s))
#efficiency bonk
