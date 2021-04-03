from time import time
from functools import reduce
st,x = time(),1
for i in range(1,100):
    x *= i
print(reduce(lambda x,y : int(x) + int(y), str(x)))
print(f"Time taken : {time() - st}")
#Avg Time Taken: 9E-4 seconds