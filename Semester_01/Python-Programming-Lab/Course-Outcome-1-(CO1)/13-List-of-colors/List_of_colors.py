# Create a list of colors from comma-separated color names entered by user.Display first and last color
color = input("Enter the list of color names separated by commas:")
lst1 = color.split(",")
print("First color entered :", lst1[0])
print("Last color entered :", lst1[-1])
