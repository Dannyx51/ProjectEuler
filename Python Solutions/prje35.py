from time import time
from primeHelper import Prime

st = time()
n = 1000000

prime = Prime.genPrime(n)

count = 0
for i in range(2,n):
    gaming = True
    if prime[i]:
        si = str(i)
        for j in range(len(si)):
            if not prime[int(si[j:] + si[:j])]:
                gaming = False
                break
    else:
        gaming = False

    if gaming:
        count += 1

print(count)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.35 seconds