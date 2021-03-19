# pythin programme to copy odd lines of files to other

f1 = open("demo1.txt", "w")
f2 = open("demo2.txt", "w")
n = int(input("Enter the number of lines:"))
for i in range(n):
    f1.write(input("Enter some text:")+"\n")
# f1.write("hellowld\n")
# f1.write("samuel\n")
# f1.write("vatakara\n")
# f1.write("kozhikode\n")
f1.close()
f1 = open("demo1.txt", "r")
count = 1
for i in f1:
    if count % 2 == 0:
        count += 1
        continue
    f2.write(i)
    count += 1
f1.close()
f2.close()
