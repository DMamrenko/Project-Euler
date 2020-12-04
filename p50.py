#Project Euler Problem #50

most_consecutives = 0
longest_chain = 0

file = open('primes.txt', 'r')
primes = file.read().splitlines()

def primes_below(start, n):
    current = start
    bank = []
    while n > int(primes[current]):
        bank.append(int(primes[current]))
        current += 1
    return bank

def consecutive_primes(start, target):
    s = 0            #holds the sum, want it to reach the target
    chain = 0        #holds the length of the chain
    bank = primes_below(start, target)
    n = 0
    if bank == []:
        return 0
    while s < target:
        s += bank[n]
        n+=1
        if n == len(bank):
            return 0
        chain += 1
    if s == target:
        return chain
    elif s > target:
        if start == len(bank)-1:
            return 0
        else:
            start += 1
            return consecutive_primes(start, target)
        
for i in primes:
    chain = consecutive_primes(0, int(i))
    if chain > longest_chain:
        longest_chain = chain
        most_consecutives = i
        print("{} has a new longest chain of {} primes summed.".format(most_consecutives, longest_chain))

