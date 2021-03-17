#Create a list of colors from comma-seperated color names entered by user.Display first and last color
color=input("Enter the list of color names seperated by commas:")
print("First color entered :",color.split(",")[0])
print("Last color entered :",color.split(",")[-1])