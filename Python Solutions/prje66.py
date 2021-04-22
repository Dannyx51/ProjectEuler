maxD = 100

ls = [i ** 2 for i in range(1,maxD ** 2)]
lslen = len(ls)

dl = {}

for D in range(2,maxD+1):
    if D in ls: continue
    for i in range(lslen):
        x = ls[i]
        for j in range(lslen):
            if j >= i: break
            y = ls[j]

            if x - (D * y) == 1:
                if D in dl:
                    dl[D] = i+1 if i+1 < dl[D] else dl[D]
                else:
                    dl[D] = i+1
    print(D)


fm = 0; fx = 0
for x in dl:
    if dl[x] > fm:
        fm = dl[x]
        fx = x

print(fm, fx)