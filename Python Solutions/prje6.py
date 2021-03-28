from time import time

st = time()

ps = pt = 0
for i in range(1,101):
    ps += i
    pt += i ** 2

print((ps ** 2) - pt)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 