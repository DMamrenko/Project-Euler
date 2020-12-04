#Project Euler Problem 85: Counting Rectangles
#Dennis Mamrenko
class Pair():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def area(self):
        return self.first*self.second
    def rectCount(self):
        m = self.first
        n = self.second
        return (m * n * (n + 1) * (m + 1)) // 4
    def display(self):
        return ('Length: {} | Width: {} | Rectangle Count: {} | Area: {}'.format(pair.first, pair.second, pair.rectCount(), pair.area()))
    
difference = 2000000
pairs = []
for i in range(30, 60):
    for j in range(30, 60):
        pair = Pair(i, j)

for i in pairs:
    if abs(2000000 - i.rectCount()) < difference:
        difference = 2000000 - i.rectCount()
        best = i
        print(i.display())
        
