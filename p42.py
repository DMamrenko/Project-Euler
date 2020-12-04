s = 0
greatest = 0
count = 0
tris = []
file = open("p42.txt", 'r')
words = file.readline().split("\",\"")
  
def let_to_num(c):
    return (ord(c))-64

for i in range(1, 200):
    tris.append((i*(i+1))/2)
    
for word in words:
    for letter in word:
        s+=let_to_num(letter)
    if s > greatest:
        greatest = s
    if s in tris:
        count+=1
    s = 0
print(greatest)
  


