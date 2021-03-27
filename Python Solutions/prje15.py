from time import time

st = time()
#only change this n value
n = 20

#dont touch anything from here
n += 1
g = [[0 for i in range(n)] for j in range(n)]  

for i in range(n):
    g[0][i] = 1
    g[i][0] = 1 

for x in range(1,n):
    for y in range(1,n):
        g[x][y] = g[x-1][y] + g[x][y-1]

print(g[n-1][n-1])
print(f"Time taken : {time() - st}")
#Avg Time taken = 0.006s
