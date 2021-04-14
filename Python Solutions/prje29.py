from time import time

st = time()

l = set()
for a in range(2,101):
    for b in range(2,101):
        l.add(a**b)

print(len(l))
print(f"Time taken : {time() - st}")
#Avg Time Taken: 6E-3 seconds