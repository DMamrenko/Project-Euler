#Project Euler Problem 38

for i in range(9387, 9235, -1):
    result = ''.join(sorted("{}{}".format(str(i), str(i*2))))
    if result == "123456789":
        print("{}{}".format(str(i), str(i*2)))
        break
