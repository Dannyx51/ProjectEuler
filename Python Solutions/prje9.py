from time import time

st = time()

for m in range(1,1000):
    for n in range(1,m):
        a = (m**2) - (n**2)
        b = 2 * m * n
        c = (m**2) + (n**2)
        
        if (a + b + c) > 1000: break

        if(a + b + c) == 1000:
            print(a * b * c)
            break
    
print(f"Time taken : {time() - st}")
#Avg Time Taken: 2E-3 seconds

# Problem:
    # A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a**2 + b**2 = c**2
    # For example, 32 + 42 = 9 + 16 = 25 = 52.
    # There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    # Find the product abc.

# Solution:
    # Any pythagorean triple can be formed using the following method:
        # Take two numbers, m and n for which n is always less than m.
            # a = (m**2) - (n**2)
            # b = 2 * m * n
            # c = (m**2) + (n**2)
    # Increment m and n until you generate a triple whos sum is 1000