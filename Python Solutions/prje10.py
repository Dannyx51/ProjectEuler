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

lp = []
for i in range(2, len(prime)):
    if prime[i] == True:
        lp.append(i)

total = 0
for i in lp:
    total += i
print(total)