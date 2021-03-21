#only change this n value
n=20

#dont touch anything from here
n += 1
g = [[0 for i in range(n)] for j in range(n)]  

for i in range(n):
    #print(i)
    g[0][i] = 1
    g[i][0] = 1 

for x in range(1,n):
    for y in range(1,n):
        g[x][y] = g[x-1][y] + g[x][y-1]

def print2D():    
    for y in g:
        for x in y:
            print(x,end = " ")
        print()

print(g[n-1][n-1])


