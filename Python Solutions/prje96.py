# mmmmmmm this might be the problem i enjoy the most
# Sudoku Solver!!!

# Check Axis Functions
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

# Get Axis Functions
def mY(l:list, ind:int) -> list:
    return l[ind]
def mX(l:list,ind:int) -> list:
    tl = [[0 for i in range(9)] for j in range(9)]
    for x in range(9):
        for y in range(9):
            tl[x][y] = l[y][x]
    return tl[ind]
def mSquare(l:list, ind:int) -> list:
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
    return tl[ind]

# Utility Functions
def getS(y:int,x:int) -> int:
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
def printGame(l:list) -> None:
    print(*l, sep = '\n')
def printMaps(map:list) -> None:
    for i in range(9):
        print(*map[i], sep='\n')
        print()

# Map Related Functions
def updateMaps(bMap:list, gameBoard:list) -> list: # updates maps with possible locations of each number
    
    # validate columns and rows
    for z in range(9):
        for n in range(9):
            if z + 1 not in chy(gameBoard,n):
                for x in range(9):
                    bMap[z][n][x] = 0
            if z + 1 not in chx(gameBoard,n):
                for y in range(9):
                    bMap[z][y][n] = 0

    for z in range(9):
        for y in range(9):
            for x in range(9):
                s = getS(y,x)

                if z+1 not in chs(gameBoard,s):
                    bMap[z][y][x] = 0

    for y in range(9):
        for x in range(9):
            if gameBoard[y][x]:
                for z in range(9):
                    bMap[z][y][x] = 0

    return bMap
def evalMaps(map:list) -> list: # returns a dict of {number : # of possible positions left for number}
    ret = {}
    for z in range(9):
        c = 0
        for y in map[z]:
            c += sum(y)
        if c:
            ret[z+1] = c
    return ret
def iterate(boolMap:list,gameBoard:list) -> tuple:
    
    for z in range(9):
        for y in range(9):
            for x in range(9):
                if boolMap[z][y][x]:
                    s = getS(y,x)
                    curS = mSquare(boolMap[z],s)
                    if curS.count(1) == 1: # if this is the only place it can go in this square
                        boolMap[z][y][x] = 0
                        gameBoard[y][x] = z + 1
                        boolMap = updateMaps(boolMap,gameBoard)
                    if mX(boolMap[z],x).count(1) == 1: # if this is the only place in this column where it can go
                        boolMap[z][y][x] = 0
                        gameBoard[y][x] = z + 1
                        boolMap = updateMaps(boolMap,gameBoard)
                    if mY(boolMap[z],y).count(1) == 1: # if this is the only place in this row where it can go
                        boolMap[z][y][x] = 0
                        gameBoard[y][x] = z + 1
                        boolMap = updateMaps(boolMap,gameBoard)
    return boolMap, gameBoard

ltxt = [x.replace('\n','') for x in open('Python Solutions\\prje96_sudoku.txt').readlines()]
l = [ltxt[i:i+9] for i in range(1,len(ltxt),10)]

for z in range(len(l)):
    for i in range(len(l[z])):
        l[z][i] = [int(x) for x in l[z][i]]

# I'm using a 3d boolean array as a map of where i can place what number
# Z index : index + 1 is the number that the map is validates
#->  as in index 0 = a 2d map of positions where the number 1 can be placed
# Y,X     : just the y,x coord on the map
# curind = 0
# for gameBoard in l:
#     boolMap = [[[1 for i in range(9)] for j in range(9)] for k in range(9)]
#     dm = evalMaps(boolMap)

#     depth = 100
#     while(len(dm) != 0):
#         if not depth:
#             print(f"uh oh!, check {curind}'s solution'")
#             break
#         boolMap = updateMaps(boolMap, gameBoard)
#         boolMap, gameBoard = iterate(boolMap, gameBoard)
#         dm = evalMaps(boolMap)
#         depth -= 1
#     if not depth: 
#         curind += 1
#         continue

#     print("\n Finished! ")
#     print()
#     printGame(gameBoard)
#     curind += 1


# Debugging area, should be commented out in final
gameBoard = l[2]
boolMap = [[[1 for i in range(9)] for j in range(9)] for k in range(9)]
dm = evalMaps(boolMap)
while(len(dm) != 0):
    boolMap = updateMaps(boolMap, gameBoard)
    boolMap, gameBoard = iterate(boolMap, gameBoard)
    printGame(gameBoard)
    
    input("\nPress Enter to Continue...")
    dm = evalMaps(boolMap)