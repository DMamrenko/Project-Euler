#Project Euler - #50
with open('primes.txt') as f:
    p = f.read()
    primes = [int(s) for s in p.split()]

# strictly consecutive from 2
# total = 0
# for i, prime in enumerate(primes):
#     if total in primes:
#         print(total, "is a prime. Made up of", i, "consecutive primes: ")
#     total += prime


# finding the 21 consecutive equaling 953 
# being 953 [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
# found = False
# current = 0
# while not found:
#     found = sum(primes[current:current+21]) == 953
#     print(found, sum(primes[current:current+21]), primes[current:current+21])
#     current += 1

total = 0
for i in range(3, 546):
    total += primes[i]

print(total)
print(total in primes)
print(primes[-1])

# print(*primes, sep="\n")
