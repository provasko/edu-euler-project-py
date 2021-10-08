# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# First lets made logic for 9009
n = 9009
# start from 99 coun
# for i in range (99, 0, -1):

i = 91
j = 99

a = n // 1000
b = (n % 1000) // 100
c = (n % 100) // 10
d = n % 10

if a == d and b == c:

    print(n)
