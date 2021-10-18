# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Create algorithm for 13 (sixth prime number)
n = 0
lst = []
k = 0
for i in range(2, 10000):
    for j in range(2, i):
        if i % j == 0:
            k += 1
    if k == 0:
        lst.append(i)
        n += 1
    else:
        k = 0
print(lst[n-1])
