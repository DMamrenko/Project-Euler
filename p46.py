#Project Euler Problem 46
primes = [2, 3]
def is_prime(n):
    mid = n+1 // 2
    for i in range(2, mid):
        if n % i == 0:
            return False
    return True

def primes_below(n):
    if n > primes[-1]:
        for i in range(primes[-1]+2, n):
            if is_prime(i):
                primes.append(i)
            i+=2
    return primes

def breaks_conjecture(n, pbn):
    base = 1
    for i in pbn:
        while i+2*(base**2) != n:
            if i+2*(base**2) < n:
                base +=1
            elif i+2*(base**2) > n:
                base = 1
                break
        if i+2*(base**2) == n:
            return False
    return True


for i in range(9, 1000001, 2):
    if not is_prime(i) and breaks_conjecture(i, primes_below(i)):
        print(i)
        break



            
