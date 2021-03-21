
i = 0
m = 0
while True:
    i += (42840)
    for j in range(2,21):
        if i % j != 0:
            break   
        elif j == 20:
            m = i
    if m != 0:
        break

print(m)
