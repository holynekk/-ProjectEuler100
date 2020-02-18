#Sieve_of_Eratosthenes


x = 110000
primes = [True]*x
p = 2
while p < x**0.5:
    if primes[p]:
        for k in range(p*2,x,p):
            primes[k] = False
    p += 1
prime_no = []
for y in range(len(primes)):
    if primes[y]:
        prime_no.append(y)
for _ in range(int(input())):
    say = int(input())
    print prime_no[say+1]






