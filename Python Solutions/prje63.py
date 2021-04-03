from time import time

st = time()

l = set()
for i in range(1,30):
    for n in range(2,30):
        if len(str(i**n)) == n:
            l.add(i**n)
            print(i,n)

