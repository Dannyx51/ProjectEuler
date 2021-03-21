import time
from math import *

st = time.time()

count = 0
for n in range(23,101):
  for r in range(1,n):
    s = factorial(n) / (factorial(r) * factorial(n-r))
    if s > 1000000:
      count += 1

print(count)
#print(factorial(5) / (factorial(3) * factorial(5-3)))

print("Runtime: " + str(time.time()-st))
