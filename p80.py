#Project Euler Problem 80
from math import sqrt, floor
from decimal import *

lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
total = 0
def sum_digits(n):
    total = 0
    s = str(n)
    for i in s:
        total += int(i)
    return total

for i in range(1, 100):
    if i not in lst:
        getcontext().prec = 102
        print(str(Decimal(i).sqrt())[3:], len(str(Decimal(i).sqrt())[3:]),  sum_digits(str(Decimal(i).sqrt())[3:]))

print(total)
