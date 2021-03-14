#purpose - program to perform some list operations
list1 = []
list2 = []
print("Select operation.")
print("1.Check Length of two list's are Equal")
print("2.Check sum of two list's are Equal")
print("3.whether any value occur in both ")
print("4.Display Lists")

while True:
    choice = input("Enter any choice ")
    if choice in ('1', '2', '3', '4'):
        list1Len = int(input("Enter the number of elements in list 1 : "))
        for i in range(0, list1Len):
            print("Enter the element ", i+1, ":")
            item1 = int(input())
            list1.append(item1)
        list2Len = int(input("Enter the number of elements in list 2 : "))

        for j in range(0, list2Len):
            print("Enter the element ", j+1, ":")
            item2 = int(input())
            list2.append(item2)

        if choice == '1' :
           if len(list1) == len (list2):
                 print(" Length are Equal")
           else :
                 print(" Length are Not Equal")
        
        if choice == '2':
             if sum(list1) == sum (list2):
                 print(" Sums are Equal")
             else :                 
                 print("  Sums are Not Equal")
      
        if choice == '3':
         list3 =[x for x in list1 if x in list2]
         print("Common elements in both list's are \n", list3) 
      
        if choice == '4':
         print( "List 1 is :\n",list1 ," List 2 is :\n", list2)                       

