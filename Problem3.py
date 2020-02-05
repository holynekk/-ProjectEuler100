a = int(input())
for i in range(a):
    b = int(input())
    q = 2
    while q**2 <= b:
        while b % q == 0:
            if b/q == 1:
                break
            else:
                b /= q
        q += 1
    print b

