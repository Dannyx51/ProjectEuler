from time import time

lperi = []
m = 2
while m < 10:
    for n in range(1,m):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n **2
        
        t = (a,b,c)
        peri = a + b + c
        
        if peri > 1000: break
        

    print((a,b,c), a+b+c)
    m += 1