#Project Euler Problem 32

products = []
total = 0
def isPandigital(mand, mult, p):
    numbers = []
    s = ("{}{}{}".format(str(mand), str(mult), str(p)))
    for n in s:
        if n not in numbers:
            numbers.append(n)
        else:
            return False
    if len(numbers) == 9 and "0" not in numbers:
        if p not in products: products.append(p)
        return True
        
    

            
for i in range(1, 10):
    for j in range(11, 9999):
        if "0" in str(j):
            continue
        elif isPandigital(i, j, i*j):
            print("New Pandigital Product: {}x{}={}".format(i, j, i*j))
            
for i in range(11, 100):
    for j in range(100, 1000):
        if "0" in str(j):
            continue
        elif isPandigital(i, j, i*j):
            print("New Pandigital Product: {}x{}={}".format(i, j, i*j))     

print('All products:', products)
print('Sum of all products:', sum(products))
