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

# 1366 - need to check whet site is working

#another variant

b = 2**1000
c = str(b)

d = []

for dig in c:

    d.append(int(dig))

e = sum(d)

print(e)
