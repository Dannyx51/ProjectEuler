from time import time

st = time()

n,d = 3,2; count = 0
for _ in range(1000):
    if len(str(n)) > len(str(d)): count += 1
    n += 2 * d
    d = n - d

print(count)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 6E-3 seconds
