from itertools import permutations
from functools import reduce
from time import time

st = time()

lDiv = [2,3,5,7,11,13,17]

s = [reduce(lambda x,y : x + y, z) for z in list(permutations("0123456789"))]

l = []
for i in range(len(s)):
    count = 0
    for j in range(1,8):
        t = int(s[i][j:j+3])
        if(t % lDiv[j-1] == 0):
            count += 1
    if(count == 7):
        l.append(int(s[i]))

print(sum(l))
print(f"Time taken : {time() - st}")
#Avg Time Taken: 15.44 seconds