# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
# set up number
n = 13195
# set up largest prime factor
d = 0
# set up counter
k = 0
# try out all the numbers from 2 to n
for i in range(2, n+1):
    # try out all numbers from 2 to actual
    for j in range(2, i):
        # count amount of factors
        if i % j == 0:
            k += 1
    # set up new d if there is no factors
    if k == 0:
        d = i
    else:
        k = 0
print(d)
