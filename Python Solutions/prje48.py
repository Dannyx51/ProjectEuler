import math
n = 1000
m = 10**10
total = sum(pow(i, i, m) for i in range(1, n + 1))
print(total % (m))

