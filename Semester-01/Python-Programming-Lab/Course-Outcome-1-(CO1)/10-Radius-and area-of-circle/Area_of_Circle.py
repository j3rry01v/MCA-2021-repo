# purpose - to find area of a circle

# normal way
PI = 3.14
r = float(input("Enter the radius of the circle: "))
area = PI * r * r
print("%.2f" % area)

# best way
import math as ma

area = ma.pi * pow(r, 2)
print("area is", area)
# use any of it
