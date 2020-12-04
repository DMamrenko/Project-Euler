#Project Euler Problem 27
biggest = 0
product = 0
hold = []
primes1 = []
primes2 = []

def f(n, a, b):
    return n*n + a*n + b

def isPrime(n):
    mid = n+1 // 2
    if n < 0:
        return False
    else:
        for i in range(2, mid):
            if n % i == 0:
                return False
    return True

for i in range(1001):
    if isPrime(i):
        primes1.append(i)
        primes1.append(-i)
        primes2.append(i)
        primes2.append(-i)        

for i in primes1:
    for j in primes2:
        n = 0
        product = i*j
        while isPrime(f(n, i, j)):
            hold.append(f(n, i, j))
            n+=1
        if len(hold) > biggest:
            biggest = len(hold)
            print(product)
        hold = [] 

