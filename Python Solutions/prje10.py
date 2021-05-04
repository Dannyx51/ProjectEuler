from time import time
from primeHelper import Prime

st = time()

ans = sum(Prime.genPrime(2000000))

print(ans)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.43~ second

# Problem:
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    # Find the sum of all the primes below two million.

# Solution:
    # See primeHelper to see how the list is generated.
    # sum the generated list.
