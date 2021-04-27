from time import time
from math import ceil, log

st = time()

number = pow(2,7830457)
number *= 28433
number += 1

sizeN = ceil(log(number, 10))
part = (sizeN // 235720) + (sizeN % 235720)
number %= 10 ** part

number = str(number)

print(number[len(number) - 10:])
print("Time taken :", time() - st)
#Avg Time Taken : 4E-2 seconds
