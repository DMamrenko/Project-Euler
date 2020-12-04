#Project Euler Problem 71
import time
from fractions import Fraction
start = time.time()
a = 3/7
b = 1/3

fracts = [Fraction(3, 7)]
for i in range(1, 100001):
    for j in range(1, i):
        f = j/i
        if f < a and f > b and j%i != 0:
            # print(j, '/', i)
            if Fraction(j, i) not in fracts:
                fracts.append(Fraction(j, i))
# print(fracts)     
fracts = sorted(fracts)
# print(fracts)
# print(fracts)
print(fracts[-2])
print(time.time()-start, 'seconds')