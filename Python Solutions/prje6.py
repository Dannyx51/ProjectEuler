
ps = pt = 0
for i in range(1,101):
    ps += i
    pt += i ** 2

print((ps ** 2) - pt)