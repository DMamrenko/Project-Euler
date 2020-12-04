#Project Euler Problem 49
valids = []
sequence = []
def isPrime(n):
    mid = n+1 // 2
    if n < 0:
        return False
    else:
        for i in range(2, mid):
            if n % i == 0:
                return False
    return True

for i in range(1001, 10000):
    if isPrime(i):
        valids.append(i)
        i+=2

for prime in valids:
    if prime == 1487:
        continue
    elif isPrime(prime+3330) and isPrime(prime+(2*3330)) and (''.join(sorted(str(prime))) == ''.join(sorted(str(prime+3330))) and ''.join(sorted(str(prime+3330))) == ''.join(sorted(str(prime+(2*3330))))):
        print("{}{}{}".format(prime, prime+3330, prime+(2*3330)))
