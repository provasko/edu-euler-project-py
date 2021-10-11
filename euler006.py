# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

a = 0
b = 0
for i in range(1, 101):
    a += i * i
    b += i
print(b*b - a)
