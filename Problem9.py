q = int(input())
for i in range(q):
    anan = []
    number = int(input())
    for a in range(1,int(number/2)+1):
        b = (number**2 - 2*number*a)/(2*number - 2*a)
        c = (number-a-(number**2 - 2*number*a)/(2*number - 2*a))
        if a < b and b < c:
            if a**2 + b**2 == c**2:
                anan.append((a*b*c))

    if anan == []:
        print -1
    else:
        print max(anan)

