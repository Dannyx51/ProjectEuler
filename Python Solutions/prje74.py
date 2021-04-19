from time import time

def dfc(n:int) -> int:
    pos = {"0":1,"1":1,"2":2,"3":6,"4":24,"5":120,"6":720,"7":5040,"8":40320,"9":362880}
    
    ret = 0
    for x in str(n):
        ret += pos[x]
    
    return ret

st = time()

gDict = {}

limit = 1000000
count = 0
for i in range(1,limit):
    l = set()
    n = i
    lSize = 0

    while n not in l:
        l.add(n)
        n = dfc(n)
        
        lSize += 1
        if lSize > 60: break
        
    if lSize == 60:
        count += 1

print(count)
print(f"{time() - st}")
