def findFirst(num):
    x = 2
    while x != num:
        if not num % x:
            if x != None : return x
        x += 1
    return num

search = 4

num = 134000 # lol i updated this every time i incremented by 1k, till i hit the number
#efficiency stonks

consec = 0
while True:
    l = set()
    n = num
    while n != 1:
        div = findFirst(n)
        # print(div)
        n //= div
        if div not in l: l.add(div)
        # print(n)

    if len(l) == search:
        consec += 1
        # print(num,consec)
    else: consec = 0
    if consec == search:
        break
    num += 1

print(num - (search - 1))
