from time import time

st = time()

i = 0
m = 0
while True:
    i += 9699690
    for j in range(2,21):
        if i % j != 0:
            break   
        elif j == 20:
            m = i
    if m != 0:
        break

print(m)
print(f"Time Taken : {time() - st}")
#Avg Time Taken: 1.1E-4 seconds
