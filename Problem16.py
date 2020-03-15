#Solve it again by using C language

a = int(input())
for i in range(a):
    total = 0
    b = int(input())
    number = str(2**b)
    for k in number:
        total += int(k)
    print total