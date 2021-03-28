from time import time

st = time()

total = 0 
for i in range(1,1000):
    if i % 3 == 0:
        total += i
        continue
    if i % 5 == 0:
        total += i

print(total)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 9.6E-4 seconds