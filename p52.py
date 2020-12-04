#Project Euler Problem 52

def sdigits(n):
    return ''.join(sorted(str(n)))

for i in range(2, 1000000):
    if sdigits(i) == sdigits(2*i) == sdigits(3*i) == sdigits(4*i) == sdigits(5*i) == sdigits(6*i):
        print(i)
        break
    
