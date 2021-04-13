from time import time

st = time()
grid = [list(map(int,x.split(','))) for x in open("Python Solutions\\prje81_matrix.txt").read().split('\n')]

for y in range(79,-1,-1):
    for x in range(79,-1,-1):
        down = right = 0
        if y != 79:
            down = grid[y+1][x]
        if x != 79:
            right = grid[y][x+1]

        if not down or not right:
            grid[y][x] += down if not right else right
        elif down > right:
            grid[y][x] += right
        else:
            grid[y][x] += down

print(grid[0][0])
print(f"Time taken : {time() - st}")
#Avg Time Taken: 6E-2 seconds
