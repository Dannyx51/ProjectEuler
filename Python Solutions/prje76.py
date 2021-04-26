from time import time

st = time()

n = 100
vals = [0 for _ in range(n+1)]
vals[0] = 1
for i in range(1,n):
    for j in range(i,n+1):
        vals[j] += vals[j - i]

print(vals[n])
print(f"Time taken : {time() - st}")
#Avg Time Taken: 2E-3 seconds
