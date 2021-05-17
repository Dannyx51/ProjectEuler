from primeHelper import genPrime, isPrime
from time import time

limit = 10000

lp = set(genPrime(limit))
searchlist = set(genPrime(pow(10,6)))

def check(a:int,b:int) -> bool:
    v1 = int(str(a) + str(b))
    v2 = int(str(b) + str(a))
    
    pv1, pv2 = False, False

    if v1 < limit: pv1 = v1 in searchlist
    else: pv1 = isPrime(v1)

    if v2 < limit: pv2 = v2 in searchlist
    else: pv2 = isPrime(v2)

    return pv1 and pv2

st = time()

exitloops = False
for a in lp:
    if exitloops: break
    for b in lp:
        if exitloops: break
        if b < a: continue
        
        if check(a,b):
            for c in lp:
                if exitloops: break
                if c < b: continue

                if check(a,c) and check(b,c):
                    for d in lp:
                        if exitloops: break
                        if d < c: continue

                        if check(a,d) and check(b,d) and check(c,d):
                            for e in lp:
                                if exitloops: break
                                if e < d: continue

                                if check(a,e) and check(b,e) and check(c,e) and check(d,e):
                                    print(a+b+c+d+e)
                                    exitloops = True

print(f"Time taken : {time() - st}")
#Avg Time Taken: 13.2~ seconds