l = []

bound = 354300
# ok so some explanations, the largest number to the fifth power is 9^5, and so the largest number produced would be x(9^5), 
# where x == length of number. 9^5 produces a 5 digit number, and 5(9^5) produces a 6 digit number. 6(9^5) also produces a 6 digit number
# (354294) to be exact, and so I set the bound just a little higher for safety

for i in range(2,bound):
    t = 0
    for j in str(i):
        t += pow(int(j),5)
    if t == i:
        l.append(i)

total = 0
for i in l:
    total += i

print(total)