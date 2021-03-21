
l = []
for i in range(1,1000):
    if i % 3 == 0:
        if l.count(i) == 0:
            l.append(i)
    if i % 5 == 0:
        if l.count(i) == 0:
            l.append(i)

total = 0
for i in l:
    total += i
print(total)