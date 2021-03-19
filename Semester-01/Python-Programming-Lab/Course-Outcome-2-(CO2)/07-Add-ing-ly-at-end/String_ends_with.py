# purpose - Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
string = input("Enter the TEXT")

if len(string) < 3:
    print(string)
elif string.endswith('ing'):
    print(string + 'ly')
else:
    print(string + 'ing')
