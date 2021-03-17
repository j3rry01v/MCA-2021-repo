# purpose Create a single string separated with space from two strings by swapping the character at position 1
string = input("Enter 2 string separated by space : ")
string = string.split(' ')
print(string[1][0] + string[0][1:] +" "+ string[0][0] + string[1][1:]  )

