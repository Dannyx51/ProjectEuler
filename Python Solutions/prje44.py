from math import sqrt
from time import time

def penta(n):
    return (n * ((3 * n )- 1)) // 2

def isPenta(n):
    x = (sqrt(1 + (24 * n)) + 1 )/ 6
    return x == int(x)

st = time()

found = False
i = 0
while not found:
    i += 1
    
    j = penta(i)

    for x in range(i-1, 0, -1):
        k = penta(x)
        if isPenta(abs(j - k)) and isPenta(j + k):
            print(abs(j - k))
            found = True
            break

print(f"Time taken: {time() - st}")
# why is it this slow