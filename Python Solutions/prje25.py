n = m = z = 1
i = 2
while(len(str(z)) != 1000):
    z = n + m
    n = m
    m = z
    i += 1

print(i)

