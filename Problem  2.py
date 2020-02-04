a = int(input())
for i in range(a):
    b = int(input())
    q = 1
    w = 2
    total = 0
    while w < b:
        if w %2 == 0:
            total += w
        q,w = w,q+w
    print total