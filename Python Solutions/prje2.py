
z = 0
n = m = 1

limit = 4000000
total = 0
while(z < limit):
    z = n + m
    n = m 
    m = z
    if z % 2 == 0:
        total += z

print(total)