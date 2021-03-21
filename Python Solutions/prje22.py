#this one is kinda iffy but ok

txt = open("C:\\Users\\dhaan\\Documents\\PythonPrjs\\ProjectEuler\\prje22_names.txt","r")
raw = txt.read()
txt.close()
raw = raw.replace("\"","")

names = raw.split(",")
names.sort()

points = []
total = 0
for i in range(len(names)):
    v = 0
    for x in names[i]:
        v += ord(x) - 64
    total += v * (i+1)

print(total)