from time import time

st = time()

n = m = z = 1
i = 2
while(len(str(z)) != 1000):
    z = n + m
    n = m
    m = z
    i += 1

print(i)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 3E-2 seconds