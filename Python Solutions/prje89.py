from functools import reduce
from time import time

st = time()

def RtoI(num:str) -> int:
    # Takes in a string roman numeral and returns in normal integer format
    sym = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    keys = list(sym)

    skip = False
    ret = 0
    for x in range(len(num)):
        cur = keys.index(num[x])
        if skip:
            skip = not skip
            continue

        if x + 1 < len(num):
            nI = keys.index(num[x+1]) 
            if nI == cur + 1 or nI == cur + 2:
                ret += sym[keys[nI]] - sym[num[x]]
                skip = True
                continue
            else:
                ret += sym[num[x]]
        else:
            ret += sym[num[x]]

    return ret

def ItoR(num:int) -> str:
    sym = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    keys = list(sym)

    ret = ""
    upC = 0
    for x in str(num)[::-1]:
        if x == "0":
            upC += 1
            continue

        up = int(x) * (10 ** upC)

        if up in sym:
            ret = sym[up] + ret
        else:
            check49 = up + (10 ** upC)
            cur = 0
            if check49 in sym:
                modifier = 1 if int(str(up)[0]) == 4 else 2
                prev = keys.index(check49) - modifier
                ret = sym[keys[prev]] + sym[check49] + ret
            else:
                if (10 ** upC) == 1000:
                    times = up // 10 ** upC
                    ret = "M"*times + ret
                else:
                    cur = sym[5 * (10 ** upC)]
                    use = sym[10 ** upC]
                    if int(str(up)[0]) > 5:
                        times = up - (5 * (10 ** upC))
                        times //= 10 ** upC
                        ret = cur + use*times + ret
                    else:
                        times = up // (10 ** upC)

                        ret = use*times + ret
                    
            
        upC += 1

    return ret

lRomGiven = open('p089_roman.txt','r').read().split("\n")

concat = len(reduce(lambda x,y: x + y, lRomGiven))

lBackToRom = list(map(ItoR,map(RtoI,lRomGiven)))

concat2 = len(reduce(lambda x,y: x + y, lBackToRom))

print(concat - concat2)
print(f"Time taken : {time() - st}")
#Avg Time Taken: 1E-2 seconds
