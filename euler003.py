# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
# set up number
n = 600851475143
# n is very big, but we can add sqrt and check only to this number
nn = int(sqrt(n))
# set up largest prime number
d = 0
# set up list from 2
lst = [2]
# try out all the numbers from 3 to nn ignoring all even numbers (all odd from 3)
for i in range(3, nn+1, 2):
    # add check for divisibility for 2 and 5
    if i > 10:
        if (i % 2 == 0) or (i % 5 == 0):
            continue
    # try out all numbers only from list from 2 to square of actual
    for j in lst:
        # break and add to list
        if j > int((sqrt(i)) + 1):
            # add check divisibility n by i
            if n % i == 0:
                d = i
            lst.append(i)
            break
        # break if not prime
        if i % j == 0:
            break
    # set up new d if prime and add to list
    else:
        if n % i == 0:
            d = i
        lst.append(i)
print(d)
