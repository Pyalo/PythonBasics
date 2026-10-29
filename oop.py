# oop -> Object Oriented Programming is a way to organize your code

# properties + function which manipulate that object
#class # template

# book title, author, isbn, price

class Book:
    #constractor == special function
     def __init__(self, title, author, isbn, price):
         self.title = title
         self.author = author
         self.isbn = isbn
         self.price = price
     def print_details(self):
         print(self.title, self.author, self.isbn, self.price)


     def apply_discount(self, discount):
         self.price = (self.price * 1 - discount/100)
         print("New Price is", self.price)


b1 = Book("River Between", "Ngugi Waithiongo", "ISB1018839",2300)
b2 = Book("UTENGANO", "Dan James", "ISB1220233", 1000)

b1.print_details()
b1.apply_discount(10)

print(b2.price)

# create class> create functions which will manipulate that object(can have several)> objects which will do something

