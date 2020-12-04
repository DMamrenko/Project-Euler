s = 0


def int_to_bin(n):
    return str(format(n, "b"))

def isPalindrome(s):
    return s[::-1] == s

for i in range(1000001):
    if isPalindrome(str(i)) and isPalindrome(str(int_to_bin(i))):
        s+=i

print(s)
