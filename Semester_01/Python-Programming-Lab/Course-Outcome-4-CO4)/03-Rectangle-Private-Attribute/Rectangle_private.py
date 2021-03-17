# purpose - Create a class rectangle with private attributes length and width. overlead '<' operator to compare the
# area of two reactangles

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


l1 = int(input("Enter the length of first rectangle"))
w1 = int(input("Enter the width of second rectangle"))
rectangle1 = (l1, w1)
l2 = int(input("Enter the length of first rectangle"))
w2 = int(input("Enter the width of second rectangle"))
rectangle2 = (l2, w2)
# r1 = Rectangle(4, 5)
# r2 = Rectangle(6, 3)
if rectangle1 < rectangle2:
    print("Area of rectangle 1 is smaller")
else:
    print("Area of rectangle 2 is smaller")
