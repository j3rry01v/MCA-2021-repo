#purpose - to promt user list of integers and promt over if greater than 100
ListofInt = []
print(" This list can add upto 10 elements")
print("\n")
for i in range (1, 10) :
    a = int(input("Enter the number "))
    if a < 100 :
        ListofInt.append(a)
    else:
        ListofInt.append("over")
print(ListofInt)       