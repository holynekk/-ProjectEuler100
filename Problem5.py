#!/bin/python

a = int(input())
for i in range(a):
    b = int(input())
    q = [1,2]
    if b == 2:
        print 2
        continue
    if b == 1:
        print 1
        continue
    for k in range(3,b+1):
        for t in q:
            if k == 1:
                break
            elif k % t == 0:
                k /= t
        if k == 1:
            continue
        else:
            q.append(k)
    result = 1
    for y in q:
        result *= y
    print result






