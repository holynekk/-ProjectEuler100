def fact(number):
    if number == 1:
        return 1
    return number*fact(number-1)


a = int(input())
for i in range(a):
    n, m = list(map(int, raw_input().split()))
    print(fact(n+m)//(fact(n)*fact(m)) % (10**9+7))
