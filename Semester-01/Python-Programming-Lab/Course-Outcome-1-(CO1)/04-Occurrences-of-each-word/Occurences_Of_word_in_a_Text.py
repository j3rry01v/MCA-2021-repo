# purpose Count the occurrences of each word in a line of text
text = input("\nEnter any text")
toFindWord = input("\nEnter a word to find")
a = []
count = 0
a = text.split(" ")
for i in range(0, len(a)):
    if toFindWord == a[i]:
        count = count + 1
print("\nCount of the word is:")
print(count)
