def penta(n):
    return (n * ((3 * n )- 1)) // 2

def found(l) -> tuple:
    for j in l:
        for k in l:
            s = j + k
            d = abs(j - k)

            if s in l and d in l:
                return (True,s,d)
    return (False,0,0)

l = [i+1 for i in range(10)]
l = list(map(penta,l))

n = 11
ret = (False,0)
while not found(l)[0]:    
    l.append(penta(n)); n += 1
    print(l)

print(found(l)[0])