a = int(input())
for i in range(a):
    b = int(input())
    b3 = (b-1) / 3
    b5 = (b-1) / 5
    b15 = (b-1) / 15
    print 3*b3*(b3+1)/2 + 5*b5*(b5+1)/2 - 15*b15*(b15+1)/2
