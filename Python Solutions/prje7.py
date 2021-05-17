from time import time
from primeHelper import genPrime

st = time()

prime = genPrime(1000000) 

print(prime[10000])
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.33 seconds

# Problem:
    # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    # What is the 10001st prime number?

# Solution:
    # Generate a list of primes under 1 million (there are more than 10k primes in this range)
        #   See the code of primeHelper.py to understand how I'm generating a list of primes.
    # print the 10000th index as all indices are actually one behind actual