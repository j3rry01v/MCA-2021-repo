#purpose to merge two dictionaries
def Merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
Merge(dict1, dict2)
print("Merge done \n ", dict2)