# Starting in the top left corner of a 2×2 grid, and only being able to move to the
# right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

n = int(input())
n2 = n * 2
x = 2 ** n
print(x)

y = 2 ** n + 2 ** n - 2 ** (n-1)
print(y)

# need to google Binomial coefficient
# for position (a, b) it is = (a+b)!/((b!*((a+b)-b))! = (a+b)!/a!*b!
verh = 1
for i in range(1, n2+1):
    verh *= i

niz = 1
for j in range(1, n):
    niz *= j

z = verh/(niz * niz)
print(z)
