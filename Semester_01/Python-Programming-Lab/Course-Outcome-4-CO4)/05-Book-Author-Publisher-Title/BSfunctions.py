# functions for book shop program

#  function for choice 1
class BSfunctios :
 def addBook(self,flist):
    aflag = False
    mflag = False

    choice = int(input("1.Add at position 2.Add at end : "))
    id = input("Enter id :")
    bname = input("Enter Book name : ")
    auth = input("Enter author name : ")
    price = input("Enter the price : ")
    pages = input("Enter pages : ")
    bk = id + "," + bname + "," + auth + "," + price + "," + pages
    if (choice == 1):
        pos = int(input("Enter the position : "))
        flist.insert(pos, bk)
        if (mflag == False):
            mflag = True
        else:
            if aflag == False:
                aflag = True
                flist.append(bk)
        print("Book Details added successfully .")
    # ---------------------------------------------------------


# function for choice 7

  def writefile(self,flist):
    if mflag == True:
        print("Over-writing the data......")
        with open("bookdata.dat", "w") as fh:
            for i in fh:
                fh.write(i)
    elif aflag == True:
        print("Appending new data.......")
        with open("bookdata.dat", "a") as fh:
            for i in flist[datalen:]:
                fh.write(i)
    else:
        print("Exiting......")


# ---------------------------------------------------------
# function for choice 2
  def deleteBook(self,flist, id):
    mflag = False
    pos = 0
    for b in flist:
        if b.split(",")[0] == id:
            flist.pop(pos)
            if (mflag == False):
                mflag = True
            print("Deleted successfully..")
            break
        pos = pos + 1
    else:
        print("Book with ", id, "not found.")


# -----------------------------------------------------------
# function for choice 3
  def modifyBook(self,flist, id, pr):
    mflag = False
    pos = 0
    for b in flist:
        lst = b.split(",")
        if lst[0] == id:
            lst[3] = pr
            flist[pos] = ",".join(lst)
            if mflag == False:
                mflag = True
            print("Modification done successfully..")
            break
        pos = pos + 1
    else:
        print("Book with ", id, "not found.")


# ------------------------------------------------
# function for choice 4
  def dispauth(self,flist, authname):
    for a in flist:
        lst = a.split(",")
        if lst[2] == authname:
            print(lst)
    else:
        print("no more author details found....")


# -----------------------------------------------
# function for choice 6
  def priauth(self,flist, price):
    choic = input("Choose 1.Less than entered price, 2.Greater than entered price : ?")
    if (choic == 1):
        for a in flist:
            lst = a.split(",")
            if float(lst[3]) <= float(price):
                print(lst)
    else:
        for a in flist:
            lst = a.split(",")
            if float(lst[3]) > float(price):
                print(lst)
# import sys
# import BSfunctions as f
#
# fh = open("bookdata.dat")
# flist = fh.readlines()
# fh.close()
# datalen = len(flist)
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








