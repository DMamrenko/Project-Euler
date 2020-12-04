#Project Euler Problem 44
import math

def isPentagonal(n):
    hold = (math.sqrt((24*n) + 1) + 1)/6
    return hold == int(hold)

def pen(n):
    return n*((3*n)-1)/2

for k in range(1, 1000000):
    for j in range(1, k):
        if isPentagonal(pen(k)+pen(j)) and isPentagonal(pen(k)-pen(j)):
            print(pen(k)-pen(j))
            break
            
