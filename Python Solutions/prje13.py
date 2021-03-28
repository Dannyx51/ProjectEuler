from functools import reduce
from time import time

st = time()

raw = open("Python Solutions\\prje13_num.txt","r").readlines()

total = reduce(lambda x,y: int(x) + int(y), [x.replace('\n','') for x in raw])

print(str(total)[0:10])
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0 seconds??

#idk either, it keeps saying 0 - 9.9E-4 so like im gonna run with the funnier number