a = 600851475143
i = 2
while i ** 2 < a:
    while a % i == 0:
        a = a / i
    i = i + 1

print(a)