from time import time

def pal(var):
    svar = str(var)
    return svar == svar[::-1]

#converts to bin
def dectobin(n):
    return bin(n).replace("0b","")

st = time()

l = []
for i in range(1,1000001):
    if pal(i) and pal(dectobin(i)):
        l.append(i)

print(sum(l))
print(f"Time taken : {time() - st}")
#Avg Time Taken: 0.35 seconds