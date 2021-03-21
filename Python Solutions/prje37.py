n = 1000000 #im hoping that this has the set im looking for in it

prime = [True for i in range(n+1)] 
p = 2
while (p * p <= n): 
        
    # If prime[p] is not changed, then it is a prime 
    if (prime[p] == True): 
            
        # Update all multiples of p 
        for i in range(p * p, n+1, p): 
            prime[i] = False
    p += 1
prime[1] = False

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

total = 0
for i in l:
  total += i
print(total)

#ayy my n value worked but barely
