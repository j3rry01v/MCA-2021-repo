def area(length, width, height):
    length = int(input("Enter the length of Cuboid"))
    height = int(input("Enter the Breadth of Cuboid"))
    width = int(input("Enter the Height of Cuboid"))
    return 2 * (length * width + width * height + height * length)


def perimeter(length, width, height):
    length = int(input("Enter the length of Cuboid"))
    height = int(input("Enter the Breadth of Cuboid"))
    width = int(input("Enter the Height of Cuboid "))
    return 4 * (length + width + height)


def volume(length, width, height):
    return length * width * height
