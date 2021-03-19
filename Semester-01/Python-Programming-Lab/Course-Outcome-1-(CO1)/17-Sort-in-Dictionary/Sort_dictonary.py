# user inpupt section - errror in this
# """ dictCount = int(input("Enter the number of dictionary values"))
# dictItem = {}
# for i in range(dictCount) :
# name = input()
# values int(input())
# dictItem[name] = values
#  ""
#
dict1 = {}
print(type(dict1))
limit = int(input("Enter  the limit"))
for i in range(limit) :
    dict1.update({input("Enter the key") : input("Enter the value")})
# dictItem = {'apple': 40, 'orange': 2, 'banana': 1, 'lemon': 3}

l = list(dict1.items())  # dict to list conversion
l.sort()
print("\n Ascending order is", l)  # sorted list

l = list(dict1.items())
l.sort(reverse=True)  # sorting in reverse order
print("\nDescending order is", l)

dict  = dict(l)  # list to dict

print("\nDictionary", dict)
print(("dict is" , dict1))
