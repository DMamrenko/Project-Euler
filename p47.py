#Project Euler Problem 47

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for i in range(1, 1000000):
    if 4 == len(set(prime_factors(i))) == len(set(prime_factors(i+1))) == len(set(prime_factors(i+2))) == len(set(prime_factors(i+3))):
        print("{}: Prime Factors:{}".format(i, prime_factors(i)))
        print("{}: Prime Factors:{}".format(i+1, prime_factors(i+1)))
        print("{}: Prime Factors:{}".format(i+2, prime_factors(i+2)))
        print("{}: Prime Factors:{}".format(i+3, prime_factors(i+3)))
        break
