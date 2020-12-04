longest = 0
value = 0
def cycle_length(d):
    s = "9"
    if d%2 == 0 or d%5 == 0:
        return 0
    else:
        while int(s)%d != 0:
            s += "9"
    return len(s)

for i in range(2, 1001):
    if cycle_length(i) > longest:
        longest = cycle_length(i)
        value = i

print("{} has {} repeating digits in its fraction form.".format(value, longest))
