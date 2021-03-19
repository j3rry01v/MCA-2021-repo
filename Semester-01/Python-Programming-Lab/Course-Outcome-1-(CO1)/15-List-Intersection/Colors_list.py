# purpose - Print out all colors from color-list1 not contained in color-list2.
colorList1 = []
colorList2 = []
finalList = []

colorList1Count = int(input("Total elements in list one :"))
for i in range(colorList1Count):
    value = input("Enter a color")
    colorList1.append(value)
colorList2Count = int(input("Total elements in list two :"))

for i in range(colorList2Count):
    value = input("Enter a color : ")
    colorList2.append(value)

list3 = [color for color in colorList1 if color not in colorList2]
print("Colors on list one which are not in list two are \n", list3)


