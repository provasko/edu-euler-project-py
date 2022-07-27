'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. 
What is the sum of the digits of the number 2^1000?
'''

total = 0
a = 2**1000

while a > 0:
    b = a % 10
    total += b 
    a = a // 10

print(total)