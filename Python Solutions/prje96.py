# mmmmmmm this might be the problem i enjoy the most
# Sudoku Solver!!!


def chy(l:list, ind:int) -> set:
    full = set([1,2,3,4,5,6,7,8,9])

    tl = []
    for i in l:
        tl.append(full.difference(set(i)))

    return tl[ind]
def chx(l:list, ind:int) -> set:
    full = set([1,2,3,4,5,6,7,8,9])

    tl = [[0 for i in range(9)] for j in range(9)]
    for x in range(9):
        for y in range(9):
            tl[x][y] = l[y][x]

    for i in range(len(tl)):
        tl[i] = full.difference(set(tl[i]))
    
    return tl[ind]
def chs(l:list, ind:int) -> set:
    full = set([1,2,3,4,5,6,7,8,9])

    tl = []
    for y in range(0,9,3):
        t1,t2,t3 = [],[],[]
        for x in range(0,9,3): # x,y is the top right corner of a square
            t1.append(l[y][x:x+3])
            t2.append(l[y+1][x:x+3])
            t3.append(l[y+2][x:x+3])
        # print(t1,t2,t3, sep = '\n')
        
        for i in range(3):
            s = t1[i]
            s.extend(t2[i])
            s.extend(t3[i])
            tl.append(s)
    
    for i in range(len(tl)):
        tl[i] = full.difference(set(tl[i]))

    return tl[ind]

def getS(y:int,x:int):
    if x < 3:
        if y < 3:
            return 0
        elif y < 6:
            return 3
        else:
            return 6
    elif x < 6:
        if y < 3:
            return 1
        elif y < 6:
            return 4
        else:
            return 7
    else:
        if y < 3:
            return 2
        elif y < 6:
            return 5
        else:
            return 8

ltxt = [x.replace('\n','') for x in open('Python Solutions\\prje96_sudoku.txt').readlines()]
l = [ltxt[i:i+9] for i in range(1,len(ltxt),10)]
gameBoard = l[0]

for i in range(len(gameBoard)):
    gameBoard[i] = [int(x) for x in gameBoard[i]]


# I'm using a 3d boolean array as a map of where i can place what number
# Z index : index + 1 is the number that the map is validates
#->  as in index 0 = a 2d map of positions where the number 1 can be placed
# Y,X     : just the y,x coord on the map
boolMap = [[[1 for i in range(9)] for j in range(9)] for k in range(9)]

# validate columns and rows
for z in range(9):
    for n in range(9):
        if z + 1 not in chy(gameBoard,n):
            for x in range(9):
                boolMap[z][n][x] = 0
        if z + 1 not in chx(gameBoard,n):
            for y in range(9):
                boolMap[z][y][n] = 0

for z in range(9):
    for y in range(9):
        for x in range(9):
            s = getS(y,x)

            if z+1 not in chs(gameBoard,s):
                boolMap[z][y][x] = 0

for i in range(9):
    print(*boolMap[i], sep='\n')
    print()