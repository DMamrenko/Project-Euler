#Project Euler Problem 69
best = 0
bestn = 1
def factors(n):
    factors = [1, n]
    midpoint = (n+1)//2
    for i in range(2, midpoint+1):
        if n%i == 0:
            factors.append(i)
    return sorted(factors)

def find_coprimes(n):
    coprimes = 0
    ftrs = factors(n)
    for i in range(1, n):
        ifactors = factors(i)
        inter = list(set(ftrs).intersection(ifactors))
        if inter == [1]:
            coprimes += 1
    return coprimes

for i in range(2, 1000):
    if (i/find_coprimes(i))>best:
        best = (i/find_coprimes(i))
        bestn = i

print(bestn)
