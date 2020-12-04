# Electrical Outlets

iterations = int(input())
for i in range(iterations):
    outlets = [int(s) for s in input().split()]
    print(outlets, sum(outlets))
    