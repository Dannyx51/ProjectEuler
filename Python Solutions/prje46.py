from time import time
from primeHelper import isPrime

st = time()

i = 3
while True:
    found = True
    isP = isPrime(i)
    if not isP:
        for x in range(1,i):
            n = i - 2 * (x ** 2)
            
            if isPrime(n):
                found = False
                break
        
    if found and not isP:
        print(f"<< {i} >>")
        break
    i += 2

print(f"Time taken : {time() - st}")
#Avg Time Taken: 2E-2 seconds