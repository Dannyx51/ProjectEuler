from primeHelper import Prime
from time import time

st = time()

n = 1000; limit = 1000000

lp = Prime.genPrime(n,noBool = True)
tot = {}

pGenTime = time()
for i in lp:
    lr = Prime.relativePrime(i)
    tot[i] = i - 1
    tot[2 * i] = tot[i]

    exp = 2
    while pow(i,exp) <= limit:
        if pow(i,exp) in tot: 
            exp += 1
            continue
        tot[pow(i,exp)] = pow(i,exp) - pow(i,exp - 1)
        exp += 1

    for x in lr[1:]:
        t = x * i
        if t > limit or t in tot: continue
        if x in tot:
            tot[t] = (tot[i] * tot[x])

print(f"Time taken to generate all the possibles from primes: {time() - pGenTime}")
print(limit - len(tot))

# Fill in the gaps
# for i in range(2,limit):
#     st = time()
#     if i not in tot:
#         tot[i] = Prime.relativePrime(i,tot=True)
#     z = time() - st    
#     if z > 0.0001: print(i, z)

# for i in tot:
#     tot[i] = i / tot[i]

# mt = 0; mi = 0
# for i in tot.items():
#     if i[1] > mt:
#         mi = i[0]
#         mt = i[1]

# print(mi,mt)
# print(f"Time taken : {time() - st}")
