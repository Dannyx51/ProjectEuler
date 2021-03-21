import time

st = time.time()

file = open("p067_triangle.txt", "r+")
raw = file.readlines()
file.close()

for i in range(len(raw)):
  raw[i] = raw[i][:len(raw[i])-1]
  raw[i] = raw[i].split(" ")
  for j in range(len(raw[i])):
    raw[i][j] = int(raw[i][j])

for i in range(len(raw)):
  if(len(raw[i])) < len(raw[len(raw)-1]):
    while(len(raw[i]) < len(raw[len(raw)-1])):
      raw[i].append(0)

def check(n, m):
  if n > m:
    return n
  elif m > n:
    return m
  else: return n

#creating a temp list bc t is nicer to type than raw
#plus its not really the raw data anymore
t = raw[:]
del raw

for y in range(len(t)-2,-1,-1):
  for x in range(y,-1,-1):
    t[y][x] += check(t[y+1][x],t[y+1][x+1])

print(t[0][0])
print(time.time()-st)
