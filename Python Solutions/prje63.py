from math import ceil
from time import time

# Establishing bounds
# --> 10^(n-1) <= x^n < 10^n
# --> n - 1 <= log(x)n
# --> (n - 1)/n <= log(x)n
# --> 10^((n-1)/n) <= x
# --> --> lim as n approaches infinity == 1
# --> --> lim of 10^((n-1)/n) == 10

st = time()

lower = 0; cur = 0; n = 1;
while lower < 10:
    lower = ceil(10**((n-1)/n))
    cur += 10 - lower
    n += 1

print(cur)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 8E-5 seconds
