from time import time

st = time()

ml = 0
md = 1
for i in range(1,1000):
    cv = 1
    cl = 0
    q = {0:0}
    while cv not in q:
        cl += 1
        q[cv] = cl
        cv = (cv % i) * 10
    
    if not cv: continue

    cl -= q[cv]

    if cl > ml:
        ml = cl
        md = i

print(md)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 2.7E-3 seconds