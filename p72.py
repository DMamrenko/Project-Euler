from fractions import Fraction

fracts = []
for i in range(1, 1000001):
    for j in range(i, 1000001):
        if i<j and Fraction(i, j) not in fracts:
            fracts.append(Fraction(i, j))
        if i % 50000 == 0:
            print(i)

print(len(fracts))
