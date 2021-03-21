import time
from math import *

s = time.time()

#just a hunch that since we're going to the 6th iteration, we start at this bad boy for efficiency
i = 123456
while True:
  gaming = True
  for ii in range(6,1,-1):
    if(not set(str(i)) == set(str(i * ii))):
      gaming = False
  if gaming: 
    print(i)
    break
  i += 1

print("Runtime: " + str(time.time()-s))
