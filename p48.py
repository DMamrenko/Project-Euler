n = 10405071317
for i in range(11, 1001):
    n+=(i**i)
s = str(n)
print(s[-10:])
