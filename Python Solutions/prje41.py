from itertools import permutations
raw = list(permutations("1234567"))

n = 7654321

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
for i in range(7123456, len(prime)):
    if prime[i] == True:
        lp.append(i)

l = []
for i in raw:
    s = ""
    for j in i:
        s += j
    l.append(int(s))

lpan = []  
for i in l:
    gaming = False
    for ii in lp:
        if i % ii == 0:
              gaming = True
              break
    if gaming:
        lpan.append(i)   

lpan.sort()
print(lpan[len(lpan) - 1])

#idfk it works