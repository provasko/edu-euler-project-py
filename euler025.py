# The Fibonacci sequence is defined by the recurrence relation
# The 12th term, F12, is the first term to contain three digits. 144
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

proverka = 0
poryadok = 2
a = 10**999
chislo = 1
chislo2 = 1
x = 0

while proverka < 1:

    x = chislo + chislo2
    chislo2 = chislo
    chislo = x
    proverka = chislo // a
    poryadok += 1

print(poryadok)

# 4782
