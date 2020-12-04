#Project Euler Problem 43
from itertools import permutations
total = 0

def hasProperty(n):
    s = str(n)
    two = int(s[1:4])
    three = int(s[2:5])
    five = int(s[3:6])
    seven = int(s[4:7])
    eleven = int(s[5:8])
    thirteen = int(s[6:9])
    seventeen = int(s[7:])
    return two%2 == 0 and three%3 == 0 and five%5 == 0 and seven%7 == 0 and eleven%11 == 0 and thirteen%13 == 0 and seventeen%17 == 0

perms = [''.join(p) for p in permutations('0123456789') if p[0]!='0']
for i in perms:
    n = int(i)
    if hasProperty(n):
        total +=n 
print("Finished: ", total)
