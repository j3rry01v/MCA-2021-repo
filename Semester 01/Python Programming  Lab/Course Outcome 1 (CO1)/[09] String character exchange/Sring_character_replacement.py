#purpose -Create a string from given string where first and last characters exchanged.

string = input("Enter a string :  ")
print("\n String after replacing first ans last character" ,string[-1]+string[1:-1]+string[0])