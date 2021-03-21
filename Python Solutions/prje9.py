l = []
for m in range(1,1000):
    for n in range(1,1000):
        if n >= m: break
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        if((a + b + c) > 1000): break
        #print(a+b+c)
        if((a + b + c) == 1000):
            print(a, b, c, a * b * c)