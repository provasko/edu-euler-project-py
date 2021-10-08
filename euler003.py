# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
# set up number
n = 13195
# set up largest prime number
d = 0
# set up empty list
lst = []
# set up counter
k = 0
# try out all the numbers from 2 to n
for i in range(2, n+1):
    # try out all numbers from 2 to actual
    for j in lst:
        # break if not prime
        if i % j == 0:
            break
    # set up new d if prime and add to list
    else:
        d = i
        lst.append(i)
print(d)
