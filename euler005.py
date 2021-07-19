# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

for a in range(2520, 1000000000, 20):
    if a % 20 == 0 and a % 19 == 0 and a % 18 == 0 and a % 17 == 0 and a % 16 == 0 and a % 15 == 0 and a % 14 == 0 and a % 13 == 0 and a % 12 == 0 and a % 11 == 0:
        print(a)
        break

# 232792560
