#Project Euler Problem 45
import math
def tri(n):
    return (n*(n+1))//2

def isPentagonal(n):
    hold = (math.sqrt((24*n) + 1) + 1)/6
    return hold == int(hold)

def isHexagonal(n):
    hold = (math.sqrt((8*n) + 1) + 1)/4
    return hold == int(hold)

for i in range(286, 1000000):
    if isPentagonal(tri(i)) and isHexagonal(tri(i)):
        print(tri(i))
        break


