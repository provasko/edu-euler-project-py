# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Create algorithm for 13 (sixth prime number)
from math import sqrt
stop_point = 10001
n = 0
lst = []
k = 0
for i in range(2, 1000000):
    if (i > 10):
        if (i % 2 == 0) or (i % 10 == 5):
            continue
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            n += 1
            break
        if i % j == 0:
            break
    else:
        lst.append(i)
        n += 1
    if n == stop_point:
        break
print(lst[n-1])

# 104743
