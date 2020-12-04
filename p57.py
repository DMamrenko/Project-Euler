#Project Euler Problem 57
numerators = [3, 7]
denominators = [2, 5]

def create_nums():
    index = 1
    while index < 1000:
        numerators.append(2*numerators[index]+numerators[index-1])
        index += 1 

def create_dens():
    index = 1
    while index < 1000:
        denominators.append(2*denominators[index]+denominators[index-1])
        index += 1


create_nums()
create_dens()
count = 0
for i in range(1000):
    if len(str(numerators[i]))>len(str(denominators[i])):
        count += 1
print(count)
