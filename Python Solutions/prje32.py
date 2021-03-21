# came back to it after a while, decided that the way i was attempting to solve this is too slow (permutations requires more time than the math itself)
# we need 'a * b = c' where a b c concatonated include all digits 1-9 with no repeats - the function concat takes care of the concatonation while
# the function pan takes care of checking the digits. 

# we use sets instead of lists bc sets force each item to be unique and they're faster than lists to iterate

def concat(a,b,c):
    return str(a) + str(b) + str(c)

def pan(s):
    return set(s) == set('123456789')

# the set of answers
l = set()

# the two possible ways to make a 9 digit concatination is through 1 x 4 = 4 and 2 x 3 = 4, these loops check both.
for i in range(2,10):
    if not (i % 10): continue
    for x in range(1000,10000):
        if not (x % 10): continue
        n = i * x
        n = concat(i,x,n)
        if len(n) != 9: continue
        if pan(n): l.add(i*x)

for i in range(11,100):
    if not (i % 10): continue
    for x in range(101,1000):
        if not (x % 10): continue
        n = i * x
        n = concat(i,x,n)
        if len(n) != 9: continue
        if pan(n): l.add(i*x)

print(f"sum = {sum(l)}")
