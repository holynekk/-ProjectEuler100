total = 0
q = []
a =  int(input())
for k in range(a):
    b = raw_input()
    q.append(b)
x = sorted(q)
t = int(input())
ex = 0
for k in range(t):
    e = raw_input()
    p = x.index(e)+1
    for i in range(len(e)):
        ex += ord(e[i])-64
    total += ex*p
    print total
    total = 0
    ex = 0
    
