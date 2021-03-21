#sum of amicable numbers under 10000
from math import *
import time

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
total = 0
for i in range(2,10000):
    a = d(i)
    b = d(a)
    if i == b and a != b: 
        total += i

print(total)
print("Runtime: " + str(time.time() - s))