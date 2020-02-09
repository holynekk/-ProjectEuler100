#!/bin/python


def palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def triple(number):
    for k in range(100,1001):
        if number % k == 0:
            if len(str(number/k)) < 3:
                return False
            elif len(str(number/k)) == 3:
                print k
                print number/k
                return True


a = int(input())
for i in range(a):
    b = int(input()) -1
    q = True
    while q:
        if palindrome(b):
            if triple(b):
                print b
                q = False
            else:
                b-=1
        else:
            b -= 1