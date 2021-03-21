import math

l = []
bound = 2540161
#similar to what i did in prje30, 9! = 362880, x(9!), 7(9!) gives us a number with the same length, W
for i in range(3,bound):
    t = 0
    for j in str(i):
        t += math.factorial(int(j))
    if t == i:
        l.append(i)

total = 0
for i in l:
    total += i

print(total)