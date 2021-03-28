from functools import reduce
from time import time
st = time()
print(reduce(lambda x,y: int(x) + int(y),str(pow(2,1000))))
print(f"Time taken: {time() - st}")
#python moment - literally a one liner
#Avg Time Taken: 5E-4 s
