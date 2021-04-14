from itertools import permutations
from time import time

st = time()

print("".join(list(permutations("0123456789"))[999999]))
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.6~ seconds