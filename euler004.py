# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# First lets made logic for 9009
x = 999
# start from 999 countdown two loops until we ll find palindrome
for i in range(1, 999):

    for j in range(i // 2, -1, -1):
        k = i - j
        l = x - j
        m = x - k
        n = l * m
        a = n // 100000
        b = (n % 100000) // 10000
        c = (n % 10000) // 1000
        d = (n % 1000) // 100
        e = (n % 100) // 10
        f = n % 10
        if a == f and b == e and c == d:
            break
            print(n)

# hide first logic below
# i = 91
# j = 99

# a = n // 1000
# b = (n % 1000) // 100
# c = (n % 100) // 10
# d = n % 10

# if a == d and b == c:

#     print(n)
