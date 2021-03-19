colorList1 = []
colorList2 = []
colorList1Count = int(input("Total elements in list one :"))
for i in range(colorList1Count):
    value = input("Enter a color")
    colorList1.append(value)
colorList2Count = int(input("Total elements in list two :"))

for i in range(colorList2Count):
    value = input("Enter a color : ")
    colorList2.append(value)
set1=set(colorList1)
set2 =set(colorList2)
print(set1.difference(set2))
