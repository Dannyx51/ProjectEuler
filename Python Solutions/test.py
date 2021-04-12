#test file to just try some algos and stuff without dealing with the rest of the project files

def strMulti(a:str, b:str) -> str:
    ret = ""
    if len(a) > len(b):
        a,b = b,a

    step = 0
    sumL = 0
    for x in a[::-1]:
        dec = 10 ** step
        for y in b[::-1]:
            s = int(x) * int(y)

        sumL += s * dec
        step += 1
    return sumL

print(strMulti("12","13"))
print(12*13)