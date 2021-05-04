from time import time

st = time()

total = 0 
for i in range(1,1000):
    total += i if not (i % 3) or not (i % 5) else 0

print(total)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 9.6E-4 seconds


# Problem: 
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    # Find the sum of all the multiples of 3 or 5 below 1000.

# Solution:
    # loops from 1 - 999 and adds the number to total if it is divisible by 3 or 5.