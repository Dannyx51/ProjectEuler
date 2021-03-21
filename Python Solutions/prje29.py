l = []

for a in range(2,101):
    for b in range(2,101):
        n = pow(a,b)
        if l.count(n) == 0:
            l.append(n)

print(len(l))