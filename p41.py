#Project Euler Problem 41
def isPrime(n):
    mid = n+1 // 2
    for i in range(2, mid):
        if n % i == 0:
            return False
    return True

def isPandigital(n):
    pandigital = []
    given = []
    s = str(n)
    for i in range(1, len(str(n))+1):
        pandigital.append(i)
    for num in s:
        given.append(int(num))
    given.sort()
    return pandigital == given

for i in range(9999999, 2, -2):
    if isPandigital(i) and isPrime(i):
        print(i)
        break

