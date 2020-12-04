#Project Euler : Digit Factorial Chains

from math import factorial

def findNext(n):
    s = str(n)
    total = 0
    for i in s:
        total += factorial(int(i))
    return total

def findChain(n):
    length = 0
    used = [n]
    while len(list(set(used))) == len(used):
        used.append(findNext(n))
        n = findNext(n)
    return len(used)

chains = 0       
for i in range(1, 1000000):
    if findChain(i)-1 == 60:
        chains += 1
    if i % 10000 == 0:
        print(i, 'completed')

print(chains)
