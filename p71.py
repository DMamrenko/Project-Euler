#Project Euler Problem 71
from fractions import Fraction
fracts = []
for i in range(1, 1000001):
    for j in range(1, 1000001):
        if i < j and i/j < Fraction(3, 7) and j%i != 0:
            fracts.append(Fraction(i, j))      
fracts= sorted(fracts)
print(fracts[-2])