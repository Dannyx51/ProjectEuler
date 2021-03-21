def isPal(n):
    s = str(n)
    return s == s[::-1]

l = [True for i in range(10001)]

for i in range(1,len(l)):
    if not l[i]: continue

    a,b = i, int(str(i)[::-1])

    c = 0
    while c < 50:
        if isPal(a+b):
            l[i] = False
            break
        a += b
        b = int(str(a)[::-1])   
        c += 1
    
fin = len([x for x in range(len(l)) if l[x]]) - 1
print(fin) # -1 because 0 is true and i cba to fix it up above, this is easier
