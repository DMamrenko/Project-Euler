import itertools
cubes = [i**3 for i in range(1, 1000)]


def as_list(n):
    return [int(s) for s in str(n)]

def as_int(lst):
    result = ''
    for n in lst:
        result += str(n)
    return int(result)

def get_permutations(n):
    lst = as_list(n)
    perms = list(set(itertools.permutations(lst)))
    permutations = [as_int(i) for i in perms]
    return permutations

def get_count(n):
    perms = get_permutations(n)
    total = 0
    ps = []
    for p in perms:
        if p in cubes:
            total += 1
            ps.append(p)
    print(ps, end='')
    return total

def main():
    found = False
    current = 1010
    while not found:
        count = get_count(current**3)
        if count > 1:
            print(current, count)
        if count == 5:
            found = True
            print('FOUND :', current, count)
        current += 1


if __name__ == "__main__":
    main()