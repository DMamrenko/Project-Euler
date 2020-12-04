#Project Euler Problem 39
import math
from collections import Counter
triples = []
ps = []
checks = 0
def is_ptriple(l):
  return l[0]**2 + l[1]**2 == l[2]**2

def perimeter(l):
  if l[0] + l[1] + l[2] <= 1000 and l[0] + l[1] + l[2] % 2 == 0:
    ps.append(l[0] + l[1] + l[2])
  
for a in range(3, 998):
  for b in range(a, 998):
    for c in range(b, 998):
      checks += 1
      if is_ptriple([a, b, c]) and sorted([a,b,c]) not in triples:
        triples.append([a, b, c])
        perimeter([a, b, c])
        break
print("Checks: ", checks)       
print(Counter(ps).most_common(1))
