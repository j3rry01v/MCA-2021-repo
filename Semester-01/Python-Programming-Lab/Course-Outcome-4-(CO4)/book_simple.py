"""
Create class publisher(name). Derive class Book from publisher with attrubutes title and auther .Derive class python
from Book with attributes price and no_of_pages . Write a program that displays information about a python book. Use
a base class constructor invocation and methode overriding
"""


class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher

    def display(self):
        print("Publisher name:", self.publisher)


class Book(Publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title of the book :", self.title)
        print("Author of the book:", self.author)


class Python(Book):
    def __init__(self, pub, author, title, price, no):
        self.price = price
        self.no_of_pages = no
        Book.__init__(self, title, author)
        Publisher.__init__(self, pub)

    def display(self):
        super().display()
        print("Price of the book:", self.price)
        print("Number of pages in the book", self.no_of_pages)


b1 = Python("SPD", "Brian Jones ", "Python Cookbook: Recipes For Mastering Python", 1670, 1230)
b1.display()
