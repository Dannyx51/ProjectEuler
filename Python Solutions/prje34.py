from math import factorial
from time import time

st = time()

ans = 0
bound = 2540161 #similar to what i did in prje30, 9! = 362880, x(9!), 7(9!) gives us a number with the same length, W
for i in range(3,bound):
    t = 0
    for j in str(i): 
        t += factorial(int(j))
    if t == i: ans += i
        
print(ans)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 17.7 seconds
