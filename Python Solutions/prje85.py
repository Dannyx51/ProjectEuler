from time import time

def res(n:int,m:int): # returns the number of rectangles in grid of size [N,M]
    ret = n * (n + 1) * m * (m + 1)
    ret //= 4
    return ret

st = time()

limit = 2000000

# range of sideLengths = 1 < s < 2000
maxL = 2000
mn = 0; mm = 0; md = 100000
for n in range(1,maxL):
    for m in range(1,maxL):
        cur = res(n,m)
        if cur > limit: break

    c = res(n,m-1)        # the number just under limit
    tc = res(n,m)         # the number just over limit

    dc = abs(limit - c)   # How far is under from limit
    dtc = abs(limit - tc) # how far is over from limit

    if dtc < dc:          # swap vars if over is better than under
        c,tc = tc,c
        dc,dtc = dtc,dc

    if dc < md:           # compare and set if this is closer than prev found
        md = dc
        mn = n
        mm = m - 1

print(mm * mn)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 5E-2 seconds
