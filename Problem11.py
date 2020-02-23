anan = []
baban = [0]

for i in range(20):
    anan.append(list(map(int,raw_input().split())))
for k in range(20):
    anan[k] += [0,0,0]
    anan[k] = [0,0,0] + anan[k]
for o in range(3):
    anan.append(26*[0])
for y in range(20):
    for x in range(3,23):
        if anan[y][x]*anan[y][x+1]*anan[y][x+2]*anan[y][x+3] > baban[-1]:
            baban.append(anan[y][x]*anan[y][x+1]*anan[y][x+2]*anan[y][x+3])
        if anan[y][x]*anan[y+1][x+1]*anan[y+2][x+2]*anan[y+3][x+3] > baban[-1]:
            baban.append(anan[y][x]*anan[y+1][x+1]*anan[y+2][x+2]*anan[y+3][x+3])
        if anan[y][x]*anan[y+1][x]*anan[y+2][x]*anan[y+3][x] > baban[-1]:
            baban.append(anan[y][x]*anan[y+1][x]*anan[y+2][x]*anan[y+3][x])
        if anan[y][x]*anan[y+1][x-1]*anan[y+2][x-2]*anan[y+3][x-3] > baban[-1]:
            baban.append(anan[y][x]*anan[y+1][x-1]*anan[y+2][x-2]*anan[y+3][x-3])

print baban[-1]







