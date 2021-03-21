txt = open("C:\\Users\\dhaan\\Documents\\PythonPrjs\\ProjectEuler\\prje13_num.txt","r")
raw = txt.readlines()
txt.close()
#print(raw)

total = 0
for i in raw:
    total += int(i) 

print(str(total)[0:10])
