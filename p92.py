#Project Euler Problem 92
arrive89 = 0

def square_digits(n):
    s = str(n)
    summ = 0
    for i in s:
        summ += int(i)**2
    return summ

def go(n):
    hold = [n]
    while n != 1 and n != 89:
        n = square_digits(n)
        hold.append(n)
    return hold[-1] == 89

for i in range(2, 10000000):
    if go(i):
        arrive89 += 1
print(arrive89)

