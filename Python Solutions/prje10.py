from time import time
from functools import reduce

st = time()
#sigh what is it with this site and generating primes
#i remember my original version, it was genuinely terrible
#i will use better practices this time

n = 2000000
prime = [True for i in range(n+1)] 
p = 2
while (p * p <= n): 
        
    # If prime[p] is not changed, then it is a prime 
    if (prime[p] == True): 
            
        # Update all multiples of p 
        for i in range(p * p, n+1, p): 
            prime[i] = False
    p += 1

ans = reduce(lambda x,y: x + y,[x for x in range(len(prime)) if prime[x]])

print(ans)
print(f"Time taken : {time() - st}")
#Avg Time Taken: ~1 second