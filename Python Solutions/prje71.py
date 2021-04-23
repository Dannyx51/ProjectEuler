from time import time

st = time()

search = 1000000
for d in range(2,search):
    if not d % 3: continue
    n = round(d / 3)
    n += 2 * d

    if n > search: break
    md, mn = n, d

print(f"Target:      3 / 7      -> {3/7}")
print(f"Found : {mn} / {md} -> {mn/md}")
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.15~ seconds
