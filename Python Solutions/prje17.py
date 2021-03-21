#does this even need to fully coded out, pretty sure i can do this math on paper

#I broke something but it used to work idk

def add1(v):
    n = int(v)
    if (n > 0 and n < 4) or n == 6 : return 3
    elif n == 4 or n == 5 or n == 9: return 4
    elif n == 0: return 0
    else: return 5

def add2(n):
    v = str(n)
    if len(v) == 1:
        return add1(n)
    else:
        o = int(v[1])
        t = int(v[0])

    if n < 20:
        if n == 11 or n == 12: return 6
        elif n == 15 or n == 16: return 7
        elif n == 13 or n == 14 or n == 18 or n == 19: return 8
        elif n == 10: return 3 
        else: return 9 
    else:
        if t == 2 or t == 3 or t == 8 or t == 9: return 6 + add1(o)
        elif t == 6 or t == 4 or t == 5: return 5 + add1(o)
        else: return 7 + add1(o)

def add3(n):
    v = str(n)
    h = int(v[0])
    to = int(v[1:])

    if to == 0:
        return add1(h) + 7
    else:
        return add1(h) + add2(to) + 10
fin = 0 
for i in range(1001):
    leni = len(str(i))

    if leni == 4:
        fin+= 11
    elif leni == 1:
        fin += add1(i)
    elif leni == 2:
        fin += add2(i)
    elif leni == 3:
        fin += add3(i)
print(fin)  