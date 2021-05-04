from time import time

def isP(n):
    return str(n) == str(n)[::-1]
    
st = time()

ans = 0
for i in range(100,1000):
    for j in range(100,1000):
        n = i * j
        if isP(n):
            ans = n if n > ans else ans

print(ans)
print(f"Time taken : {time() - st}")
#Avg Time Taken: ~0.44 second

# Problem:
    # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    # Find the largest palindrome made from the product of two 3-digit numbers.

# Solution:
    # Multiply every combination of a 3 digit number * 3 digit number
    # If the result (n) is palindromic, check to see if it's bigger than anything found previously
    # return the largest (n) found.