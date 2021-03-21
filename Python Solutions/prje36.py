
#function that checks for palindrom
def pal(var):
    svar = str(var)
    fh = svar[0:len(svar)//2]
    sh = svar[len(svar)//2 if len(svar) % 2 == 0 else ((len(svar)//2)+1):]
    if fh == sh[::-1]:
        return True
    else: return False

#converts to bin
def dectobin(n):
    return bin(n).replace("0b","")

l =[]
for i in range(1,1000001):
    if pal(i) and pal(dectobin(i)):
        l.append(i)

total = 0
for i in l:
    total += i
print(total)