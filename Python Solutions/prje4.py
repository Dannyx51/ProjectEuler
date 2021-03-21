
def isP(n):
    s = str(n)
    if len(s) % 2 != 0:
        a = s[0:len(s)//2]
        b = s[len(s)//2+1:]
    else:
        a = s[0:len(s)//2]
        b = s[len(s)//2:]
        #if n == 906609: print(a , b)
    return(a == b[::-1])
    
l = []
for i in range(100,1000):
    for j in range(100,1000):
        n = i * j
        #if n == 906609: print(isP(n))
        if isP(n):
            l.append(n)
l.sort()
print(l[len(l)-1])