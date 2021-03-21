
clen = 0
hlen = 0
hn = 0

for i in range(2,1000000):
    num = i
    while num != 1:
        clen += 1
        if num % 2 == 0:
            num /= 2
        else: 
            num = (num * 3) + 1
    if clen > hlen:
        hlen = clen 
        hn = i 
    clen = 0
    print(i)

print(str(hn) + ", " + str(hlen))

