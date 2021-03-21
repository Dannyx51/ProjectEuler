from itertools import permutations


# i originally made this on a chromebook, so some of the stuff is gonna be icky bc of power issues i worked around
lDiv = [2,3,5,7,11,13,17]

s = list(permutations("0123456789"))

for i in range(len(s)):
    t = ""
    for x in s[i]:
        t += x
    s[i] = t
print("Done Converting!")
print()

l = []
for i in range(len(s)):
    count = 0
    for j in range(1,8):
        t = int(s[i][j:j+3])
        if(t % lDiv[j-1] == 0):
            count += 1
    if(count == 7):
        l.append(int(s[i]))

total = 0
for i in l:
    total += i
print(total)

#worked first try baybeeeeeeee
