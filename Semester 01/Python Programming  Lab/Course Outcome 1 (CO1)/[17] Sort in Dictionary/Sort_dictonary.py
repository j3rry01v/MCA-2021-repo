#user inpupt section - errror in this
""" dictCount = int(input("Enter the number of dictionary values"))
dictItem = {}
for i in range(dictCount) :
name = input()
values int(input())
dictItem[name] = values
 """
dictItem={'apple':40,'orange':2,'banana':1,'lemon':3} 
                                         
l=list(dictItem.items())   #dict to list conversion
l.sort()  
print("\n Ascending order is",l) #sorted list 

l=list(dictItem.items())
l.sort(reverse=True) #sorting in reverse order
print("\nDescending order is",l)

dict=dict(l) #list to dict

print("\nDictionary",dict) 