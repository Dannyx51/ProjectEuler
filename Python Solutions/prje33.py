from math import gcd
d, n = 1, 1

for i in range(1,10):
    for x in range(1,i):
        for a in range(1,x):
            if ((a * 10 + i) * x) == (a * (i * 10 + x)):
                d *= x
                n *= a
                
print(d / gcd(n,d))
