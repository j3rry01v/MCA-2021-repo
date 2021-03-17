from Graphics import Circle as c
from Graphics import Rectangle as r
from Graphics.ThreeDG import Cuboid as cd
from Graphics.ThreeDG import Sphere as sp

# sample test
# print(c.area(4))
# print(c.perimeter(4))
# print(r.area(3, 6))
# print(r.area(5, 9))
# print(cd.area(4, 6, 7))
# print(cd.perimeter(5, 7, 8))
# print(sp.area(5))
# print(sp.perimeter(4))

# user input
while True:
    print("\n❖ ❖ ❖ ❖ ❖ ❖ ❖ SELECT ANY TO PERFORM OPERATION  ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖\n")
    option = int(input("\n 1. Rectangle \n 2.Circle \n 3.Cuboid \n 4.Sphere\n"))
    print("❖ ❖ ❖ ❖ ❖ ❖ ❖ SELECT ANY TO PERFORM OPERATION  ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖")
    if option == 1:
        print("❖ ❖ ❖ ❖ ❖ ❖ ❖ RECTANGLE OPERATIONS  ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖")
        rectOption = int(input("\n 1.Area \n 2.Perimeter \n"))
        if rectOption == 1:
            length = int(input("Enter the length of Rectangle \t"))
            breadth = int(input("Enter the Breadth Rectangle\t"))
            print("Area is ", r.area(length, breadth))
        elif rectOption == 2:
            length = int(input("Enter the length of Rectangle \t"))
            breadth = int(input("Enter the Breadth of Rectange\t"))
            print("Perimeter is ", r.perimeter(length, breadth))
        else:
            print("Invalid Option !")
    if option == 2:
        print("❖ ❖ ❖ ❖ ❖ ❖ ❖ CIRCLE OPERATIONS  ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖")
        circOption = int(input("\n 1.Area \n 2.Perimeter \n"))
        if circOption == 1:
            r = int(input("Enter the Radius \t"))
            print("Area of Circle with radius ", r, "is ", c.area(r))
        elif circOption == 2:
            r = int(input("Enter the Radius \t"))
            print("Perimeter of the circle with radius ", r, "is", c.perimeter(r))
        else:
            print("Invalid Option !")
    if option == 3:
        print("❖ ❖ ❖ ❖ ❖ ❖ ❖ CUBOID OPERATIONS  ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖")
        qubOption = int(input("\n 1.Area \n 2.Perimeter \n 3.Volume \n"))
        if qubOption == 1:
            length = int(input("Enter the length of Cuboid \t"))
            width = int(input("Enter the Height of Cuboid\t"))
            height = int(input("Enter the Breadth of Cuboid\t"))
            print("Surface Area of Cuboid is ", cd.area(length, width, height))
        elif qubOption == 2:
            length = int(input("Enter the length of Cuboid\t"))
            width = int(input("Enter the Height of Cuboid\t"))
            height = int(input("Enter the Breadth of Cuboid\t"))
            print("Perimeter of Cuboid is ", cd.perimeter(length, width, height))
        elif qubOption == 3:
            length = int(input("Enter the length of Cuboid\t"))
            width = int(input("Enter the Height of Cuboid\t"))
            height = int(input("Enter the Breadth of Cuboid\t"))
            print("Volume of Cuboid is ", cd.volume(length, width, height))
        else:
            print("Invalid Option !")
    if option == 3:
        print("❖ ❖ ❖ ❖ ❖ ❖ ❖ SPHERE OPERATIONS  ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖ ❖")
        sphOption = int(input("\n 1.Area \n 2.Perimeter \n 3.Volume \n"))
        if sphOption == 1:
            r = int(input("Enter the Radius\t"))
            print("Area of Sphere with radius ", r, "is", sp.area(r))
        elif sphOption == 2:
            r = int(input("Enter the Radius\t"))
            print("Perimeter of Sphere with radius ", r, "is", sp.perimeter(r))
        elif sphOption == 3:
            r = int(input("Enter the Radius\t"))
            print("Volume of Sphere with radius ", r, "is",sp.volume(r))
    else:
        print("Invalid Option !")
