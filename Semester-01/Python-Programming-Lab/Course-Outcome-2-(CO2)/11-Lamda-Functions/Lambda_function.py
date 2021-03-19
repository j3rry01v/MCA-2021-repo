l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(list(filter(lambda n: n % 5 == 0, l)))

area_square = lambda side: side * side
area_rectangle = lambda length, width: length * width
area_triangle = lambda s, a, b, c: (s * (s - a) * (s - b) * (s - c)) ** 0.5

a = 10
b = 20
c = 15
s = (a + b + c) / 2

print(area_square(a))
print(area_rectangle(a, b))
print(area_triangle(s, a, b, c))
