from time import time

st = time()

s = t = 0
for i in range(1,101):
    s += i
    t += i ** 2

print((s ** 2) - t)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 9.9E-4 seconds

# Problem:
    # The sum of the squares of the first ten natural numbers is: 
        # 1**2 + 2**2 + ... + 10**2 = 385 
    # The square of the sum of the first ten natural numbers is: 
        # (1 + 2 + ... + 10)**2 = 55**2 = 3025
    # Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
        # 3025 - 385 = 2640
    # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Solution:
    # 's' stores the sum of the natural numbers that are squared at the end
    # 't' stores the sum of the square of the natural numbers
    # (s**2) - t is the difference.