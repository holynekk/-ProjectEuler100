baban = []
anan = [0,0]
a = int(input())
for i in range(a):
    baban.append(int(input()))

t = max(baban)+1
prob = [True] * t

q = 2
while q < t**0.5:
    if prob[q]:
        for k in range(q*2,t,q):
            prob[k] = False
    q += 1
for o in range(2,t):
    if prob[o]:
        anan.append(anan[-1] + o)
    else:
        anan.append(anan[-1])
for p in baban:
    print anan[p]







