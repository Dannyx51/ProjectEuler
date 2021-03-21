#uses similar ideas as that of 32, except with some refined methods - lambda instead of a function for concat etc.
from functools import reduce
i = 1
exit = False
answer = 0
while True:
    l = [str(i)]
    for x in range(2,10):        
        l.append(str(i * x))

        s = reduce(lambda x,y: x + y, l)
        if x == 2 and len(s) > 9: exit = True
        if len(s) > 9: break
        if set(s) == set('123456789'):
            answer = int(s) if int(s) > answer else answer
    i += 1
    if exit: break

print(f"Max = {answer}")