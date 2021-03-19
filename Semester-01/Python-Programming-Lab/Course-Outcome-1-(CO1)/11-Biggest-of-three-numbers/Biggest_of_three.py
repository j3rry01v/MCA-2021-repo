# purpose-Find biggest of 3 numbers entered
num1 = float(input("\nEnter the first number\n"))
num2 = float(input("\nEnter the second number\n"))
num3 = float(input("\nEnter the third number\n"))
if (num1 > num2) and (num1 > num3):
    max = num1
elif (num2 > num1) and (num2 > num3):
    max = num2
else:
    max = num3
    print("the largest among three numbers is", max)
