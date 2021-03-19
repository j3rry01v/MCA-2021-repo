# purpose Create a single string separated with space from two strings by swapping the character at position 1
string = input("Enter 2 string separated by space : ")
string = string.split(' ')
# swapping two at position 1
print(string[0][0] + string[1][1] + string[0][2:] + " " + string[1][0] + string[0][1] + string[1][2:])

# swapping and making the swapped item UPPERCASE
print(string[0][0] + string[1][1].upper() + string[0][2:] + " " + string[1][0] + string[0][1].upper() + string[1][2:])
