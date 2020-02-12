#!/bin/python


t = int(raw_input().strip())
for a0 in range(t):
    n, k = raw_input().strip().split(' ')
    num = raw_input().strip()
    seq = 0
    multi = []
    for y in range(int(n)-int(k)+1):
        total = 1
        for u in num[seq:seq+int(k)]:
            total *= int(u)
        multi.append(total)
        seq += 1
    print max(multi)


