# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Took algorithm from 007

from math import sqrt

n = 0
lst = []
summ = 0
k = 0
for i in range(2, 2000000):
    if (i > 10):
        if (i % 2 == 0) or (i % 10 == 5):
            continue
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            summ += i
            n += 1
            break
        if i % j == 0:
            break
    else:
        lst.append(i)
        summ += i
        n += 1

print(lst[n-1])
print(summ)

# 142913828922
