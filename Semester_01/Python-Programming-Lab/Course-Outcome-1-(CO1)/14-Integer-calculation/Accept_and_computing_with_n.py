# purpose -Accept an integer n and compute n+nn+nnn
n = int(input("Enter the number"))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
result = n + int(t1) + int(t2)
print("The value is:", result)
