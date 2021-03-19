# purpose - Program to find the factorial of a number
num = int(input("enter a number: "))

fac = 1
i = 1

while i <= num:
    fac = fac * i
    i = i + 1

print("factorial of ", num, " is ", fac)