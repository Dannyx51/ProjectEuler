from time import time
from math import sqrt

def filter(l:list): return [int(x) for x in map(str,l) if '0' not in x]

def last2(n:int): return int(str(n)[2:])
def first2(n:int): return int(str(n)[:2])

st = time()

lTri = [(n * (n + 1) // 2) for n in range(45,10012)]  # List of 4 digit triangular numbers
lSqr = [(n ** 2) for n in range(32,100)]              # List of 4 digit square numbers
lPen = [(n * (3 * n - 1) // 2) for n in range(26,82)] # List of 4 digit pentagonal numbers
lHex = [(n * (2 * n - 1)) for n in range(23,71)]      # List of 4 digit hexagonal numbers
lHep = [(n * (5 * n - 3) // 2) for n in range(21,64)] # List of 4 digit heptagonal numbers
lOct = [(n * (3 * n - 2)) for n in range(19,59)]      # List of 4 digit octagonal numbers


# Removing the numbers that have zeroes bc yeag
lTri = filter(lTri)
lSqr = filter(lSqr)
lSqr = filter(lPen)
lHex = filter(lHex)
lHep = filter(lHep)
lOct = filter(lOct)

masterlist = [].extend(lTri,lSqr,lPen,lHex,lHep,lOct) # why did you generate them seperately if you're just gonna recombine them dan?
                                                      # idk mysterious question asker, this is how my brain works
foundset = set()

print(f"Time taken : {time() - st}")
#Avg Time Taken:  seconds