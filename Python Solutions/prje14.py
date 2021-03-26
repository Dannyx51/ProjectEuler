from time import time

hlen = 0
hn = 0
st = time()

found = {}

for i in range(2,1000000):
    num = i
    clen = 0
    while num != 1:
        if found.get(num) != None:
            clen += found.get(num)
            break

        if num % 2 == 0:
            num /= 2
        else: 
            num = (num * 3) + 1
        
        clen += 1
    found.update({i:clen})

    if clen > hlen:
        hlen = clen 
        hn = i 
    
print(str(hn) + ", " + str(hlen))
print(f"Time Taken : {time() - st}")

# 4.18427038192749