from primeHelper import Prime
from collections import Counter
from time import time

st = time()

lp = [x for x in Prime.genPrime(200000,noBool = True) if len(str(x)) - len(set(str(x))) >= 3]

def rep(s:int) -> list:
    ret = []
    s = str(s)

    for d in (Counter(s) - Counter(set(s))):
        a = ['1','2','3','4','5','6','7','8','9','0']
        temp = [int(s.replace(d,x)) for x in a if int(s.replace(d,x))]
        ret.append(temp)
    return ret

checked = set()
def validate(l:list) -> int:
    ret = []
    for i in l:
        checked.add(i)
        if Prime.isPrime(i): ret.append(i)

    return len(ret)

for i in lp:
    exit = False
    if i in checked: continue
    for x in rep(i):
        if validate(x) == 8:
            print(x[0])
            exit = True
            break
    if exit: break

print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.3~ seconds
