from time import time

st = time()

i = 0; m = 0; exitLoop = False
while not exitLoop:
    i += 9699690
    for j in range(2,21):
        if i % j: break
        exitLoop = j == 20

print(i)
print(f"Time Taken : {time() - st}")
#Avg Time Taken: 1.1E-4 seconds

# Problem: 
    # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Solution:
    # The increment for 'i' (9699690) is the multiple of all the prime numbers under 20
        # This is used for maximum efficiency, removes most of checks of divisibility
    # If a number is ever reached that can by 20, break and print said number