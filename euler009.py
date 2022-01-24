# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Euclid Elements
# a = m * m - n * n, b = 2 * m * n, c = m * m + n * n

# (m * m - n * n) + (2 * m * n) + (m * m + n * n) = 1000
# 2 * (m * m + m * n) = 1000
# m * m + m * n = 500
# D = n * n + 2000 = 0

for m in range(2, 30):
    for n in range(1, m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        summa = a + b + c
        if summa == 1000:
            print(a)
            print(b)
            print(c)
            print(a * b * c)
            break
