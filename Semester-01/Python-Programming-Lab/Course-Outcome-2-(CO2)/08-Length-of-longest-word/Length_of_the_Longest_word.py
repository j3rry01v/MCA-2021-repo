# purpose - Accept a list of words and return length of longest word
def longest(get_name):
    length = 0
    get_name = get_name.split()
    for i in get_name:
        if len(i) > length:
            length = len(i)
    return length


str = input("Enter the string: ")
word = longest(str)
print(word)
