from time import time
#An integer x is triangular exactly if 8x + 1 is a square.

def isT(n):
    banana = ((8 * n) + 1) ** 0.5
    if int(banana) == banana:
        return True
    else:
        return False

st = time()

txt = open("Python Solutions\\prje42_words.txt","r")
raw = txt.read()
txt.close()
raw = raw.replace("\"","")
lw = raw.split(',')

count = 0
for i in lw:
    n = 0
    for ii in i:
        n += ord(ii) - 64
    if isT(n):
        count += 1

print(count)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 3E-3 seconds