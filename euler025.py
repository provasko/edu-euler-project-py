# The Fibonacci sequence is defined by the recurrence relation
# The 12th term, F12, is the first term to contain three digits. 144
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

proverka = 0
a = 10**2
chislo = 1

while proverka < 0:
    chislo2 = chislo
    chislo += chislo2
    proverka = chislo // a

print(chislo2)
