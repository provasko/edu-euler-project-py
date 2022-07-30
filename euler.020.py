# Factorial digit sum

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import numbers
from tkinter import N


sum = 0
facto = 1
number1 = 10
while number1 > 0:
    facto *= number1
    number1 -= 1

while facto > 0:
    number2 = facto % 10
    facto = facto // 10
    sum += number2

print(sum)
