answer = 0
def sum_digits(s):
    result = 0
    for letter in s:
        result += int(letter)
    return result

for a in range(1, 101):
    for b in range(1, 101):
        if sum_digits(str(a**b)) > answer:
            answer = sum_digits(str(a**b))

print("Answer: {}".format(answer))
