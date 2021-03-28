from time import time

st = time()

a = 600851475143
i = 2
while i ** 2 < a:
    while a % i == 0:
        a = a / i
    i = i + 1

print(a)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 9.9E-4 seconds