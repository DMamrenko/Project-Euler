from math import sqrt
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other_point):
        return sqrt((other_point.x-self.x)**2 + (other_point.y-self.y)**2)
def Area(points):
    d1 = points[0].distance(points[1])
    d2 = points[0].distance(points[2])
    d3 = points[1].distance(points[2])
    sp = (d1+d2+d3)/2
    return (sp*(sp-d1)*(sp-d2)*(sp-d3))**0.5

def pointArea(point, points):
    a1 = Area([point, points[1], points[2]])
    a2 = Area([points[0], point, points[2]])
    a3 = Area([points[0], points[1], point])
    return (a1+a2+a3)

file = open('triangles.txt', 'r')
lines = file.readlines()
hits = 0
points = []
origin = Point(0, 0)
for i in lines:
    x, y, x2, y2, x3, y3 = [int(s) for s in i.split(',')]
    points.append(Point(x,y))
    points.append(Point(x2,y2))
    points.append(Point(x3,y3))
    if pointArea(origin, points) == Area(points):
        hits += 1
    points = []
        
p1 = Point(-1, -6)
p2 = Point(1, -1)
p3 = Point(0, 8)

print(Area([p1, p2, p3]))
print(hits)



    
