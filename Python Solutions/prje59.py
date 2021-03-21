file = open("C:\\Users\\dhaan\\Documents\\PythonPrjs\\ProjectEuler\\prje59_text.txt","r+")
raw = file.read()
file.close()

l = raw.split(",")

for i in range(len(l)):
    l[i] = int(l[i])

l1 = []
l2 = []
l3 = []

for i in range(0, len(l), 3):
    l1.append(l[i])
    l2.append(l[i+1])
    l3.append(l[i+2])

chr1 = chr2 = chr3 = 97
while True:
    gaming = False
    for i in range(len(l1)):
        n = l1[i] ^ chr1
        if !(n <= 9 and n >= 32) 
        if i == len(l1) - 1:
            gaming = True
    if not gaming: 
        chr1 += 1
    if chr1 > 122 or gaming: 
        break

print(chr1)

while True:
    gaming = False
    for i in range(len(l2)):
        n = l2[i] ^ chr2
        if n < 65: break
        if n > 90 and n < 97: break
        if n > 122: break
        if i == len(l2) - 1:
            gaming = True
    if not gaming: chr2 += 1
    if chr2 > 122 or gaming: break
print(chr2)

while True:
    gaming = False
    for i in range(len(l3)):
        n = l3[i] ^ chr3
        if n < 65: break
        if n > 90 and n < 97: break
        if n > 122: break
        if i == len(l3) - 1:
            gaming = True
    if not gaming: chr3 += 1
    if chr3 > 122 or gaming: break
print(chr3)
