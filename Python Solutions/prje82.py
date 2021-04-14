grid = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

n = 5
grid2 = [[0 for x in range(n)] for y in range(n)]
grid3 = [[0 for x in range(n)] for y in range(n)]
grid4 = [[0 for x in range(n)] for y in range(n)]

for y in range(len(grid)):
    for x in range(len(grid[0]) - 2,-1,-1):
        r = grid[y][x+1]

        if not y:
            u = 9999999
        else:
            u = grid[y-1][x+1]
        
        if y != len(grid)-1:
            d = grid[y-1][x+1]
        else:
            d = 9999999

        grid[y][x] += min(r,u,d)

print(*grid,sep='\n')