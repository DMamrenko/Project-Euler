def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)

    
def combination(n, k):
    return fact(n) // (fact(k)*fact(n-k))
x = 0
for i in range(1, 101):
    for j in range(1, i+1):
        z = combination(i, j)
        if z > 1000000:
            x += 1
            

print(x)
