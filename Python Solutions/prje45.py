def t(n):
    return int(n * (n+1)/2)

def p(n):
    return (1 + (24 * n + 1) ** 0.5) % 6 == 0

def h(n):
    return (1 + (8 * n + 1) ** 0.5) % 4 == 0

i = 286
while True:
    num = t(i)
    if p(num) and h(num):
        print(num)
        break
    i += 1


#LMAOOOOOOOO IM AN IDIOT LOOK AT BELOW

# found = False
# ts = 285
# ps = 165
# hs = 143
# final = 0 
# loops = 0
# while(not found):
#     lt = []
#     lp = []
#     lh = []

#     for i in range(1,101):
#         lt.append(t(ts + i))
#         lp.append(p(ps + i))
#         lh.append(h(hs + i))

#     for i in lt:
#         if (not found):
#             for j in lp:
#                 if (not found):
#                     for k in lh:
#                         if i == j and j == k:
#                             final = i
#                             found = True
#                             break
#                         loops += 1
#                         print(loops, i)
#                 else:
#                     break
#         else:
#             break
#     ts += 100
#     ps += 100
#     hs += 100