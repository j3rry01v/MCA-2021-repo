# purpose- removing even numbers in list
numberList = []
even_numberList = []
n = int(input("Enter the number of elements  "))

print("\n")
for i in range(0, n):
    print("Enter the element ", i + 1, ":")
    item = int(input())
    numberList.append(item)
print(" List is ", numberList)
even_numberList = [x for x in numberList if x % 2 != 0]
print("\n")
print("List after removing even numbers\n ", even_numberList)
