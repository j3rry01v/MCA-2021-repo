# purpose - to find square of n numbers
listAll = []
listSq = []
limit = int(input("Enter the number of elements in the list \n"))
for i in range(0,  limit ):
    print("Enter the element ", i+1)
    item = int(input())
    listAll.append(item)
print("List is \n", listAll)
listSq = [ x**2 for x in listAll ]
print("List after Squaring  \n ", listSq)