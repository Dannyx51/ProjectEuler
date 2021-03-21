def isP(n):
  for i in range(2,int(abs(n)**0.5)+1):
    if n % i == 0:
      return False
  return True

#--------------------------------------------------------
n = 1000
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
prime[0] = False
#--------------------------------------------------------

lp = []
for i in range(len(prime)):
  if prime[i]:
    lp.append(i)
l = list(lp)

m = 0
prod = 0
for b in lp:
  for a in lp:
    
    n = 0
    while True:
      f = n**2 + (a * n) + b
      if f not in l:
        if isP(f):
          l.append(f)
        else:
          if n - 1 > m:
            m = n - 1
            prod = a * b
            break
      n += 1

    n = 0
    while True:
      f = n**2 + (-a * n) + b
      if f not in l:
        if isP(f):
          l.append(f)
        else:
          if n - 1 > m:
            m = n - 1
            prod = -a * b
            break
      n += 1
    print(m)
print(prod)