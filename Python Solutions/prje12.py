import math

def d(n):
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0): 
            # If divisors are equal, 
            # count only one 
            if (n / i == i) : 
                count = count + 1
            else : # Otherwise count both 
                count = count + 2
    return count

def t(n):
    return (n**2 + n) // 2

j = 0
while True:
    #print(t(j))
    if(d(t(j)) > 500):
        break
    j += 1
print(t(j))