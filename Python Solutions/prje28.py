#change n to change the size of the spiral, dont touch the rest
n = 1001

m = n * n
l = [0 for i in range(m)]
for i in range(m):
    l[i] = i + 1

total = p = 0
t = 1
j = 2
for i in range(1 + 4 * ((n - 1) // 2)):
    total += l[p]
    p += j
    if t == 4:
        j += 2
        t = 0
    t += 1

print(total)