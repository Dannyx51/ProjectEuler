import time as t

st = t.time()
total = 0
for a in range(2,101):
    for b in range(2,101):
        if a % 10 == 0 or b % 10 == 0: continue
        
        n = a**b
        cur = sum([int(i) for i in str(n) if int(i)])
        total = cur if cur > total else total
print(total)
print(f"Time Taken : {t.time() - st}")
