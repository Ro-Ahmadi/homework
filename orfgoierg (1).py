
# #1.	Create a class called Person with attributes name and age.
# #Create an object of the class and print its attributes.

# class Persone:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# Mohammad=Persone("Mohammad",30)
# print(Mohammad.name)
# print(Mohammad.age)



# #2.	Add a method called greet to the person class that
# #  prints a greeting message including the person’s name.

# class Persone:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def Great(self):
#         return f"Hello, {self.name} jan How are you"

# Ahmad=Persone("Ahmad",30)
# print(Ahmad.Great())



# #3.	Create a class called Car with attributes make,
# #  model, and year. Include a method to print out the Car’s details.


# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

#     def print_details(self):
#         return f"the Car's details {self.make}, {self.model}, {self.year}"
    
# Corola=Car("Corolah 2000","Amerecan Model",2015)
# print(Corola.print_details())

# print(Corola.__dict__)




# #4.	Create a class circle with a method to compute the area.
# #  Initialize the class with the radius.

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def compute(self):
#         return 3.1415*(self.radius**2)

# circle=Circle(5)
# print(circle.compute())





# #5.	Create a class Rectangle with method to compute the area and perimeter.
# #  Initialize the class with the length and width.

# class Rectangle:
#     def __init__(self,width,Length):
#         self.width=width
#         self.Length=Length


#     def compute_area(self):
#         return self.width*self.Length
    
#     def compute_perimeter(self):
#         return 2*self.width + 2*self.Length
    
# rectangle=Rectangle(6,8)
# print(rectangle.compute_area())
# print(rectangle.compute_perimeter())




# #6.	Create a base class Animal with a method speak.
# # Create two derived classes Dog and Cat that override the speak method.

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof"
    

# class Cat(Animal):
#     def speak(self):
#         return "Meau"

# dog=Dog()
# cat=Cat()
# print("the dog is Speak ",dog.speak())
# print("the Cat is Speak ",cat.speak())


# #7. Create a base class shape with a method area.
# #  Create derive classes square and Triangle that implement
# #  the area method.

# class Shape:
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self,Length):
#         self.Length=Length

#     def area(self):
#         return self.Length**2
    
# class Triangle(Shape):
#     def __init__(self,base,heigth):
#         self.base=base
#         self.heigth=heigth

#     def area(self):
#         return 0.5*self.base*self.heigth
    
# square=Square(4)
# triangle=Triangle(4,4)

# print(f"The area of squarea is {square.area()}")
# print(f"The area of square is {triangle.area()}")



# #8. Create a class Employee with attribute name and salary.
# #  Create a drive class manager with an additional attribute department.


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary


# class Manager(Employee):
#     def __init__(self,name,Lname,salary):
#         super().__init__(name,salary)
#         self.Lname=Lname

# Hamid=Manager("Hamid","Arifi","30000")
# print(Hamid.name)
# print(Hamid.Lname)
# print(Hamid.salary)




# # #9. Create a base class vehicle with a method drive.
# # #  Create derived classes Bike and Truck that override the drive method.


# class Vehicle:
#     def drive(self):
#         pass

# class Bike(Vehicle):
#     def drive(self):
#         print("driving a Bike")



# class Truck(Vehicle):
#     def drive(self):
#         print("driving a Truck")

# truck=Truck()
# bike=Bike()

# bike.drive()
# truck.drive()




# #10.    Create a base class Bird with a method fly. 
# # create derived classes Eagle and penguin, 
# # override the fly method in penguin to indicate that penguins cannot fly.

# class Bird:
#     def fly(self):
#         pass


# class Eagle(Bird):
#     def fly(self):
#         return "Eagle is flying on the sky"

# class Penguin(Bird):
#     def fly(self):
#         return "Penguin connot flying in the sky"
    
# eagle = Eagle()
# penguin=Penguin()
# print(eagle.fly())
# print(penguin.fly())
        


# #11.	Create a class Account with private attributes balance.
# #  Provide public methods to deposit and withdraw money. 

# class Account:
#     def __init__(self,balance):
#         self.balance=balance

#     def deposit(self,amount):
#         if amount >0:
#             self.balance += amount
#             print(f"Deposited {amount} New balance: {self.balance}")

#         else:
#             print(f"Invalid depodit amount.")

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdraw {amount}. New balance: {self.balance}")

#         elif amount > self.balance:
#             print("Insufficient funds.")
#         else:
#             print("Invalid withdrawal amount")

#     def check_balance(self):
#         print(f"Currrent balance: {self.balance}")


# my_account = Account(200)
# my_account.deposit(5000)
# my_account.withdraw(100)
# my_account.check_balance()



# #12.	Create a class Book with private attributes title, author, and pages.
# #  Provide public methods to get and set these attributes. 

# class Book:
#     def __init__(self, title, author, pages):
#         self.__title = title
#         self.__author = author
#         self.__pages = pages

#     def get_title(self):
#         return self.__title

#     def set_title(self, title):
#         self.__title = title

#     def get_author(self):
#         return self.__author

#     def set_author(self, author):
#         self.__author = author

#     def get_pages(self):
#         return self.__pages

#     def set_pages(self, pages):
#         self.__pages = pages

# book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

# print("Title:", book.get_title())
# print("Author:", book.get_author())
# print("Pages:", book.get_pages())


# book.set_title("The Catcher in the Rye")
# book.set_author("J.D. Salinger")
# book.set_pages(277)
 
# print("Updated Pages:", book.get_pages())




# #13.    Create a class laptop with private attributes brand, model, and price.
# #  Private a method to apply a discount and a method to display laptop details.

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price

#     def apply_discount(self, discount_percentage):
#         if 0 <= discount_percentage <= 100:
#             self.__price *= (1 - discount_percentage / 100)
#             print(f"Discount of {discount_percentage}% applied. New price: {self.__price:.2f}")
#         else:
#             print("Invalid discount percentage.")

#     def display_details(self):
#         print(f"Brand: {self.__brand}\n Model: {self.__model}\n price: {self.__price}")


# laptop = Laptop("Apple", "MacBook Pro", 1999.99)

# laptop.display_details()

# laptop.apply_discount(10)
# laptop.display_details()



# #14
#    Create a class Bank Account with private attributes account_number 
#     and balance private methods to deposit, withdraw, and check the balance.

# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         self.__account_number = account_number
#         self.__balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Invalid ")

#     def check_balance(self):
#         print(f"Account number: {self.__account_number}")
#         print(f"Current balance: {self.__balance}")


# account = BankAccount("1256783456789", 100000.00)

# account.check_balance()

# account.deposit(20000)

# account.withdraw(50000)

# account.check_balance()

# account.withdraw(2000.00)




# #15.    Create a class student with private attributes name, grade, and age.
# # Provide method to get and set these attributes and
# # a method  to display the student’s details.

# class Student:
#     def __init__(self, name, grade, age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def get_grade(self):
#         return self.__grade

#     def get_age(self):
#         return self.__age

#     def set_name(self, name):
#         self.__name = name

#     def set_grade(self, grade):
#         self.__grade = grade

#     def set_age(self, age):
#         self.__age = age

#     def display_details(self):
#         print(f"Name: {self.__name}")
#         print(f"Grade: {self.__grade}")
#         print(f"Age: {self.__age}")


# student = Student("Mohammad Ali", 90, 18)


# print("Student Details:")
# print(f"Name: {student.get_name()}")
# print(f"Grade: {student.get_grade()}")
# print(f"Age: {student.get_age()}")


# student.set_name("Jane Smith")
# student.set_grade(85)
# student.set_age(19)



# # Display the updated student's details
# print("\nUpdated Student Details:")
# student.display_details()





# #16.	Create a class Library with attributes name and books (a list of Book objects).
# #  Provide methods to add and remove books. 
# class Library:
#     def __init__(self,name):
#         self.name=name
#         self.books = []

#     def add_books(self, Name_Book):
#         self.books.append(Name_Book)
#         print(f"Book '{Name_Book}' added")

#     def remove_book(self, Name_Book):
#         if Name_Book in self.books:
#             self.books.remove(Name_Book)
#             print(f"Book '{Name_Book}' removed")
#         else:
#             print("Invalid book in Library")

#     def print_books(self):
#         if self.books:
#             print("Books in Library:")
#             for book in self.books:
#                 print(f"- {book}")
#         else:
#             print("No books in Library")

# library = Library("Albirony")


# library.add_books("Python")
# library.add_books("C++")
# library.add_books("Java")


# library.remove_book("C++") 
# library.remove_book("C") 
   
# library.print_books() 




# #17.	Create a class School with attributes name and students (a list of Student objects).
# #  Provide methods to add and remove students. 

# class School:
#     def __init__(self,name):
#         self.name=name
#         self.students=[]

#     def add_student(self,student_name):
#         self.students.append(student_name)
#         print(f"Book '{student_name} added")

#     def remove_student(self,student_name):
#         if student_name in self.students:
#             self.students.remove(student_name)
#             print(f"Student {student_name} removed")

#         else:
#             print("No student in School")


#     def school_details(self):
#         if self.students:
#             print("Student in School:")
#             for stu in self.students:
#                 print(f"-{stu}")

#         else:
#             print("No Student in School")


# school=School("Rahman Baba")

# school.add_student("Ahamd")
# school.add_student("javad")

# school.remove_student("Ali")
# school.remove_student("javad")

# school.school_details()



# #18.	Create a class Team with attributes name and members (a list of Person objects).
# #  Provide methods to add and remove members. 

# class Team:
#     def __init__(self,name):
#         self.name=name
#         self.members=[]

#     def add_members(self,member_name):
#         self.members.append(member_name)
#         print(f"member {member_name} added")


#     def remove_member(self,member_name):
#         if member_name in self.members:
#             self.members.remove(member_name)
#             print(f"member {member_name} removed")
#         else:
#             print(f"NO {member_name} in Team")

        
#     def member_details(self):
#         if self.members:
#             for Mem in self.members:
#                 print(f"-{Mem}")

#         else:
#             print("No Member in Team")

# team=Team("Jvanan")

# team.add_members("Hamid")
# team.add_members("ali")
# team.add_members("jahan")

# team.member_details()

# team.remove_member("ali")
# team.remove_member("Ahmad")
# team.remove_member("ldsk")

# team.member_details()




# #19.	Create a class Company with attributes name and employees (a list of Employee objects).
# #  Provide methods to add and remove employees. 

# class Company:
#     def __init__(self,name):
#         self.name=name
#         self.employee=[]

#     def add_employee(self,E_name):
#         self.employee.append(E_name)
#         print(f"Employee {E_name} added")


#     def remove_employee(self,E_name):
#         if E_name in self.employee:
#             self.employee.remove(E_name)
#             print(f"employee {E_name} removed")

#         else:
#             print(f"No {E_name} in Employee")



#     def employee_details(self):
#         if self.employee:
#             for Emp in self.employee:
#                 print(f"-{Emp}")

#         else:
#             print(f"No {self.employee} in Team ")

# company=Company("Oracle")

# company.add_employee("jahan")
# company.add_employee("Emran")
# company.add_employee("Ahmad")

# company.employee_details()

# company.remove_employee("Emran")

# company.employee_details()





# #20.	Create a class Zoo with attributes name and animals (a list of Animal objects).
# #  Provide methods to add and remove animals. 

# class Zoo:
#     def __init__(self,name):
#         self.name=name
#         self.animals=[]

#     def add_animals(self,An_name):
#         self.animals.append(An_name)
#         print(f"animal {An_name}added")

#     def remove_animal(self,An_name):
#         if An_name in self.animals:
#             self.animals.remove(An_name)
#             print(f"animal {An_name} removed")

#         else:
#             print("this animal No in Zoo")


#     def animal_details(self):
#         if self.animals:
#             for An in self.animals:
#                 print(f"-{An}")

#         else:
#             print("No aninmal in the Zoo")

# zoo=Zoo("Bagh wahash")

# zoo.add_animals("wolf")
# zoo.add_animals("tiger")
# zoo.add_animals("lain")

# zoo.animal_details()

# zoo.remove_animal("lain")
# zoo.remove_animal("cat")

# zoo.animal_details()

## 21

# class FileManager:
#     def __init__(self, filename):
#         self.filename = filename

#     def read_file(self):
#         """محتوای فایل را می‌خواند و باز می‌گرداند."""
#         try:
#             with open(self.filename, 'r') as file:
#                 return file.read()
#         except FileNotFoundError:
#             print(f"خطا: فایل {self.filename} یافت نشد.")
#             return None
#         except IOError as e:
#             print(f"خطا در خواندن فایل {self.filename}: {e}")
#             return None

#     def write_file(self, content):
#         """محتوا را به فایل می‌نویسد."""
#         try:
#             with open(self.filename, 'w') as file:
#                 file.write(content)
#         except IOError as e:
#             print(f"خطا در نوشتن به فایل {self.filename}: {e}")


# filename = 'example.txt'

# file_manager = FileManager(filename)

# content_to_write = 'این یک نمونه محتوا برای نوشتن به فایل است.'
# file_manager.write_file(content_to_write)

# read_content = file_manager.read_file()

# print("محتوای خوانده شده از فایل:")
# print(read_content)

## 22















# # 21.	Create a class FileManager with methods to read from and write to a file. 
# class FileManager:
#     def __init__(self, Manager_name):
#         self.man_name = Manager_name

#     def write_to_file(self,content):
#         print(f"the file is writing by {self.man_name} ")

#     def read_from_file(self):
#         print(f"the file is reading by {self.man_name}")


# file_manager = FileManager("Manager_Ahmad")
    

# file_manager.write_to_file('This is an example content.')

# content = file_manager.read_from_file()
# if content is not None:
#     print("Content read from file:")
#     print(content)




# #22.	Create a class Log with methods to write error messages to a log file. 
# import os
# from datetime import datetime

# class Log:
#     def __init__(self, log_file):
#         self.log_file = log_file

#     def _write_message(self, message):
#         print(f"Error writing to log file: {message}")

#     def log_error(self, message):
#         formatted_message = f"ERROR: {message}"
#         self._write_message(formatted_message)

#     def log_warning(self, message):
#         formatted_message = f"WARNING: {message}"
#         self._write_message(formatted_message)

# log = Log('application.log')
    
# log.log_error('This is an error message.')
# log.log_warning('This is a warning message.')






# #23.	Create a class Config that reads configuration 
# # settings from a file and provides methods to access these settings. 

# class Config:
#     def __init__(self, config_file):
#         self.config_file = config_file
#         self.settings = self._load_config()

#     def _load_config(self):
#         print(f"Configuration file not found: {self.config_file}")

#     def get(self):
#         return f"in this program error{self.config_file}"

#     def set(self):
#         self.settings = []
#         self._save_config()

#     def _save_config(self):
#         print(f"Error writing to the configuration file: {self.config_file}")

# config = Config('config.json')
    
# print("Database Host:", config.get())

# print(config.set())

# print(config.get())




# #24.	Create a class Database that connects to a database and provides methods to execute queries.
# #  Handle exceptions if the connection fails. 
# import sqlite3
# from sqlite3 import Error

# class Database:
#     def __init__(self, db_file):
#         self.db_file = db_file
#         self.connection = None
#         self.cursor = None
#         self._connect()

#     def _connect(self):
#         try:
#             self.connection = sqlite3.connect(self.db_file)
#             self.cursor = self.connection.cursor()
#             print("Connection to database established successfully.")
#         except Error as e:
#             print(f"Error connecting to database: {e}")

#     def execute_query(self, query, params=()):
#         try:
#             self.cursor.execute(query, params)
#             self.connection.commit()
#             print("Query executed successfully.")
#         except Error as e:
#             print(f"Error executing query: {e}")

#     def fetch_all(self, query, params=()):
#         try:
#             self.cursor.execute(query, params)
#             return self.cursor.fetchall()
#         except Error as e:
#             print(f"Error fetching data: {e}")
#             return []

#     def close(self):
#         if self.connection:
#             self.connection.close()
#             print("Database connection closed.")


# db = Database('example.db')
    

# db.execute_query('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             email TEXT NOT NULL
#         );
#     ''')

# db.execute_query('INSERT INTO users (username, email) v (?, ?)', ('john_doe', 'john@example.com'))

# users = db.fetch_all('SELECT * FROM users')
# for user in users:
#     print(user)

# db.close()





# #25.	Create a class Report that generates a report from data in a file.
# #  Provide methods to handle exceptions if the file does not exist or cannot be read





# # #26.	Create a class Ticket for a movie theater with attributes movie_name, seat_number,
# # # and price. Provide methods to display ticket datails and applay discounts.
# class Ticket:
#     def __init__(self, movie_name, seat_number, price):

#         self.movie_name = movie_name
#         self.seat_number = seat_number
#         self.price = price


#     def apply_discount(self, discount_percentage):

#         if 0 <= discount_percentage <= 100:
#             discount_amount = (discount_percentage / 100) * self.price
#             self.price -= discount_amount
#             print(f"Discount applied: {discount_percentage}%")
#         else:
#             print("Invalid discount percentage. It must be between 0 and 100.")
    

#     def display_details(self):
#         details = (
#             f"Movie Name: {self.movie_name}\n"
#             f"Seat Number: {self.seat_number}\n"
#             f"Price: ${self.price:.2f}"
#         )
#         print(details)

# ticket = Ticket("The Matrix", "A12", 15.00)

# ticket.display_details()
    
# ticket.apply_discount(10) 

# ticket.display_details()




#27.	Create a class ShoppingCart with methods to add, remove, and display items.
#  Each item should be an object of a class Item with attributes name and price. 

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"{self.name} (${self.price:.2f})"

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         if isinstance(item, Item):
#             self.items.append(item)
#             print(f"Added {item} to the cart.")
#         else:
#             print("Only Item objects can be added to the cart.")

#     def remove_item(self, item_name):
#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(f"Removed {item} from the cart.")
#                 return item_name
#         print(f"Item '{item_name}' not found in the cart.")

#     def display_items(self):
#         if not self.items:
#             print("The cart is empty.")
#         else:
#             print("Shopping Cart Items:")
#             for item in self.items:
#                 print(item)


# item1 = Item("Apple", 0.99)
# item2 = Item("Bread", 2.49)
# item3 = Item("Milk", 1.89)


# cart = ShoppingCart()


# cart.add_item(item1)
# cart.add_item(item2)


# cart.display_items()




# cart.remove_item("Apple")




##28.	Create a class Restaurant with attributes name and menu (a list of Item objects).
# ##  Provide methods to add and remove items from the menu. 

# class Restaurant:
#     def __init__(self,name):
#         self.name=name
#         self.costomers=[]

#     def add_student(self,costomer_name):
#         self.costomers.append(costomer_name)
#         print(f"Book '{costomer_name} added")

#     def remove_student(self,student_name):
#         if student_name in self.costomers:
#             self.costomers.remove(student_name)
#             print(f"Student {student_name} removed")

#         else:
#             print("No student in School")


#     def school_details(self):
#         if self.costomers:
#             print("Student in School:")
#             for stu in self.costomers:
#                 print(f"-{stu}")

#         else:
#             print("No Student in School")


# school=Restaurant("Rahman Baba")

# school.add_student("Ahamd")
# school.add_student("javad")

# school.remove_student("Ali")
# school.remove_student("javad")

# school.school_details()




# #29.	Create a class Flight with attributes flight_number, destination, and passengers (a list of Person objects).
# #  Provide methods to add and remove passengers. 

# class Flight:
#     def __init__(self,flight_name,destination):
#         self.fl_name=flight_name
#         self.destination=destination
#         self.pasenger=[]

#     def add_pasenger(self,pasenger_name):
#         self.pasenger.append(pasenger_name)
#         print(f"Book '{pasenger_name} added")

#     def remove_pasenger(self,student_name):
#         if student_name in self.pasenger:
#             self.pasenger.remove(student_name)
#             print(f"pasenger {student_name} removed")

#         else:
#             print("No pasenger in Flight")


#     def Flight_details(self):
#         if self.pasenger:
#             print("pasenger in Flight:")
#             for stu in self.pasenger:
#                 print(f"-{stu}")

#         else:
#             print("No pasenger in Flight")


# flight=Flight("MaidanHavaei","To kabul")

# flight.add_pasenger("Qasim")
# flight.add_pasenger("Rahman")

# flight.remove_pasenger("Ali")
# flight.remove_pasenger("javad")

# flight.Flight_details()




# 30.	Create a class Hotel with attributes name and rooms (a list of Room objects).
#  Each Room should have attributes room_number and is_occupied.
#  Provide methods to book and checkout rooms. 

# class Hotel:
#     def __init__(self, name):
#         """Initializes the Hotel with a name and an empty list of rooms."""
#         self.name = name
#         self.rooms = []

#     def add_room(self, room):
#         """Adds a Room to the hotel's list of rooms.

#         Args:
#             room (Room): The room to add to the hotel.
#         """
#         if isinstance(room, Room):
#             self.rooms.append(room)
#             print(f"Added {room} to the hotel.")
#         else:
#             print("Only objects of type 'Room' can be added to the hotel.")

#     def book_room(self, room_number):
#         """Books a room by setting its occupancy status to True.

#         Args:
#             room_number (int): The number of the room to book.
#         """
#         room = next((r for r in self.rooms if r.room_number == room_number), None)
#         if room:
#             if not room.is_occupied:
#                 room.is_occupied = True
#                 print(f"Room {room_number} has been booked.")
#             else:
#                 print(f"Room {room_number} is already occupied.")
#         else:
#             print(f"Room {room_number} does not exist in the hotel.")

#     def checkout_room(self, room_number):
#         """Checks out a room by setting its occupancy status to False.

#         Args:
#             room_number (int): The number of the room to check out.
#         """
#         room = next((r for r in self.rooms if r.room_number == room_number), None)
#         if room:
#             if room.is_occupied:
#                 room.is_occupied = False
#                 print(f"Room {room_number} has been checked out.")
#             else:
#                 print(f"Room {room_number} is not occupied.")
#         else:
#             print(f"Room {room_number} does not exist in the hotel.")

#     def display_rooms(self):
#         """Displays all rooms in the hotel with their occupancy status."""
#         if self.rooms:
#             print(f"Rooms in {self.name}:")
#             for room in self.rooms:
#                 print(room)
#         else:
#             print(f"No rooms available in {self.name}.")

# # Example usage
# if __name__ == "__main__":
#     # # Create some Room objects
#     room1 = Room(101)
#     room2 = Room(102)
#     room3 = Room(103)
    
#     # Create a Hotel
#     hotel = Hotel("Grand Hotel")
    
#     # Add rooms to the hotel
#     hotel.add_room(room1)
#     hotel.add_room(room2)
#     hotel.add_room(room3)
    
#     # Display all rooms
#     hotel.display_rooms()
    
#     # Book a room
#     hotel.book_room(101)
    
#     # Display all rooms after booking
#     hotel.display_rooms()
    
#     # Checkout a room
#     hotel.checkout_room(101)
    
#     # Display all rooms after checkout
#     hotel.display_rooms()
 