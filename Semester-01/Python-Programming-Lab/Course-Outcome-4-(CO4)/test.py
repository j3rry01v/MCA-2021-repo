import sys
import BSfunctions as f

fh = open("bookdata.dat")
flist = fh.readlines()
fh.close()
datalen = len(flist)
choice = 0

while choice != 7:
    print("1.Add new Book")
    print("2.Delete book")
    print("3.Modify price")
    print("4.Diplay by author")
    print("5.Display all")
    print("6.Price by price")
    print("7.Exit")
    choice = int(input("enter choice : "))
    if choice == 1:
        f.addBook(flist)

    elif choice == 2:
        id = input("Enter the Book-id : ")
        f.deleteBook(flist, id)

    elif choice == 3:
        id = input("Enter Book-id : ")
        pr = input("Enter the price : ")
        f.modifyBook(flist, id, pr)

    elif choice == 4:
        authname = input("Enter author name : ")
        f.dispauth(flist, authname)
    elif choice == 5:
        print(flist)

    elif choice == 6:
        price = float(input("Enter the book price : "))
        f.priauth(flist, price)
    elif choice == 7:
        f.writefile(flist)

        sys.exit()



