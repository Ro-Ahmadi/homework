# 1. Create a class called Person with attributes name and age. Create an object of the class and print 
# #its attributes.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Creating an object of the Person class
# person1 = Person("Alice", 30)

# # Printing the attributes of the object
# print(f"Name: {person1.name}, Age: {person1.age}")


# 2. Add a method called greet to the Person class that prints a greeting message including the 
# #person's name. 
# ##2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}!")

# # Creating an object of the Person class
# person1 = Person("Alice", 30)

# # Calling the greet method
# person1.greet()

# ##3. Create a class called Car with attributes make, model, and year. Include a method to print out 
# #the car's details. 

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def car_details(self):
#         print(f"Car Details: {self.year} {self.make} {self.model}")

# # Creating an object of the Car class
# car1 = Car("Toyota", "Camry", 2022)

# # Calling the car_details method
# car1.car_details()

# #4 Create a class Circle with a method to compute the area. Initialize the class with the radius. 

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius**2

# # Creating an object of the Circle class with radius 5
# circle1 = Circle(5)

# # Computing and printing the area of the circle
# print("Area of the circle: {circle1.area:.2f}".__format__)

# ##5  Create a class Rectangle with methods to compute the area and perimeter. Initialize the class 
## with the length and width. 

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # Creating an object of the Rectangle class with length 4 and width 3
# rectangle1 = Rectangle(6, 7)

# # Computing and printing the area and perimeter of the rectangle
# print(f"Area of the rectangle: {rectangle1.area()}")
# print(f"Perimeter of the rectangle: {rectangle1.perimeter()}"  )





# # 6. Create a base class Animal with a method speak. Create two derived classes Dog and Cat that override the speak method.

# class Hiwan:
#     def __init__(self,speak):
#         self.speak = speak

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
# hewan = Hiwan()
# sag = Dog()
# cat = Cat()
# print(hewan.speak())
# print(sag.speak())
# print(cat.speak())

# 7. Create a base class Shape with a method area. Create derived classes Square and Triangle that implement the area method.

# class Shape:
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side * self.side

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def area(self):
#         return 0.5 * self.base * self.height     
# if __name__ == "__main__":
#     square = Square(4)
#     triangle = Triangle(3, 5)
#     print(f"Area of the square: {square.area()}")
#     print(f"Area of the triangle: {triangle.area()}")    

# # #8. Create a class Employee with attributes name and salary. Create a derived class Manager with an 
# #additional attribute department.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
# emp=Employee("Ali",3090)
# Ahmad=Manager("Ahmad",2401,"IS")
# print(emp.name)
# print(emp.salary)
# print(Ahmad.department)        

# ##9. Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that 
# #override the drive method. 

# class Vehicle:
#     def drive(self):
#         pass

# class Bike(Vehicle):
#     def drive(self):
#         return "Bike is being driven."

# class Truck(Vehicle):
#     def drive(self):
#         return "Truck is being driven."
# my_bike=Bike()
# truck=Truck()
# print(my_bike.drive())
# print(truck.drive())

# ##10. Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override 
# #the fly method in Penguin to indicate that penguins cannot fly. 
# class Bird:
#     def fly(self):
#         pass

# class Eagle(Bird):
#     def fly(self):
#         return "Eagle is flying high."

# class Penguin(Bird):
#     def fly(self):
#         return "Penguin cannot fly."

# b=Bird()
# e=Eagle()
# p=Penguin()
# print(p.fly())

# ##11Encapsulation and Abstraction Exercises 
# 
# #11. Create a class Account with private attributes balance. Provide public methods to deposit and 
# #withdraw money. 

# class Account:
#     def __init__(self):
#         self.__balance = 0  # private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balanc

# account=Account(20000)
# account.deposit(10000)
# account.withdraw(50000)
# account.get_balance()
# account.__balance=999999
# account.__balance(44)

# ##12 12. Create a class Book with private attributes title, author, and pages. Provide public methods to get 
## and set these attributes.
#  
# class Book:
#     def __init__(self, title, author, pages):
#         self.__title = title  # private attribute
#         self.__author = author  # private attribute
#         self.__pages = pages  # private attribute

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

# book=Book("mathmatic","Danishmand",1000)
# book.get_title()
# book.get_author()
# book.get_pages()


# book.set_titile("new title is algabr")
# book.set_author("new author is Enayet")
# book.set_pages("new pages are 470")
# print(book.get_title())
# print(book.get_author())
# print(book.get_pages())


# ##13 13. Create a class Laptop with private attributes brand, model, and price. Provide a method to apply 
# # a discount and a method to display laptop details. 

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.__brand = brand  # private attribute
#         self.__model = model  # private attribute
#         self.__price = price  # private attribute

#     def apply_discount(self, discount):
#         self.__price *= (1 - discount / 100)

#     def display_details(self):
#         print(f"Laptop: {self.__brand} {self.__model}, Price: ${self.__price:.2f}")

# ##1414. Create a class BankAccount with private attributes account_number and balance. Provide 
# #methods to deposit, withdraw, and check the balance. 

# class BankAccount:
#     def __init__(self, account_number):
#         self.__account_number = account_number  # private attribute
#         self.__balance = 0  # private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def check_balance(self):
#         return self.__balanc

# ##1515. Create a class Student with private attributes name, grade, and age. Provide methods to get and 
# #set these attributes and a method to display the student's details. 

# class Student:
#     def __init__(self, name, grade, age):
#         self.__name = name  # private attribute
#         self.__grade = grade  # private attribute
#         self.__age = age  # private attribute

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_grade(self):
#         return self.__grade

#     def set_grade(self, grade):
#         self.__grade = grade

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         self.__age = age

#     def display_details(self):
#         print(f"Name: {self.__name}, Grade: {self.__grade}, Age: {self.__age}")

# ##16Class Relationships and Advanced Concepts Exercises 
## 16. Create a class Library with attributes name and books (a list of Book objects). Provide methods 
# #to add and remove books.
#  
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []  # list to store Book objects

#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.books.append(book)
#         else:
#             print("Invalid book object. Please provide a Book instance.")

#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#         else:
#             print("Book not found in the library.")

#     def display_books(self):
#         print(f"Books in {self.name}:")
#         for book in self.books:
#             print(f"- {book.get_title()} by {book.get_author()}")

# ##17 Create a class School with attributes name and students (a list of Student objects). Provide 
## methods to add and remove students.    
#                                                                 
# class School:
#     def __init__(self, name):
#         self.name = name
#         self.students = []  # list to store Student objects

#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.students.append(student)
#         else:
#             print("Invalid student object. Please provide a Student instance.")

#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
#         else:
#             print("Student not found in the school.")

#     def display_students(self):
#         print(f"Students in {self.name}:")
#         for student in self.students:
#             print(f"- {student.get_name()}, Grade: {student.get_grade()}, Age: {student.get_age()}")
# ##18 Create a class Team with attributes name and members (a list of Person objects). Provide 
# #methods to add and remove members. 

# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.members = []  # list to store Person objects

#     def add_member(self, person):
#         if isinstance(person, Person):
#             self.members.append(person)
#         else:
#             print("Invalid person object. Please provide a Person instance.")

#     def remove_member(self, person):
#         if person in self.members:
#             self.members.remove(person)
#         else:
#             print("Person not found in the team.")

#     def display_members(self):
#         print(f"Members of Team {self.name}:")
#         for member in self.members:
#             print(f"- {member.get_name()}"

# ##19. Create a class Company with attributes name and employees (a list of Employee objects). 
# #Provide methods to add and remove employees. 

# class Company:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []  # list to store Employee objects

#     def add_employee(self, employee):
#         if isinstance(employee, Employee):
#             self.employees.append(employee)
#         else:
#             print("Invalid employee object. Please provide an Employee instance.")

#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#         else:
#             print("Employee not found in the company.")

#     def display_employees(self):
#         print(f"Employees of {self.name}:")
#         for employee in self.employees:
#             print(f"- {employee.name}, Salary: {employee.salary}")

# ##20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods 
# #to add and remove animals. 

# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []  # list to store Animal objects

#     def add_animal(self, animal):
#         if isinstance(animal, Animal):
#             self.animals.append(animal)
#         else:
#             print("Invalid animal object. Please provide an Animal instance.")

#     def remove_animal(self, animal):
#         if animal in self.animals:
#             self.animals.remove(animal)
#         else:
#             print("Animal not found in the zoo.")

#     def display_animals(self):
#         print(f"Animals in {self.name}:")
#         for animal in self.animals:
#             print(f"- {type(animal).__name__}")

# ##File Handling and Exceptions Exercises 
## 21. Create a class FileManager with methods to read from and write to a file. 

# class FileManager:
#     def __init__(self, filename):
#         self.filename = filename

#     def read_file(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 return file.read()
#         except FileNotFoundError:
#             print(f"Error: File '{self.filename}' not found.")
#         except IOError as e:
#             print(f"Error reading file '{self.filename}': {e}")

#     def write_to_file(self, data):
#         try:
#             with open(self.filename, 'w') as file:
#                 file.write(data)
#             print(f"Successfully wrote to '{self.filename}'.")
#         except IOError as e:
#             print(f"Error writing to file '{self.filename}': {e}")

# ##22. Create a class Log with methods to write error messages to a log file.     
#                    
# class Log:
#     def __init__(self, filename):
#         self.filename = filename

#     def write_log(self, message):
#         try:
#             with open(self.filename, 'a') as file:
#                 file.write(f"{message}\n")
#             print("Log entry added.")
#         except IOError as e:
#             print(f"Error writing to log file '{self.filename}': {e}")

# ##23. Create a class Config that reads configuration settings from a file and provides methods to access 
# #these settings. 

# class Config:
#     def __init__(self, filename):
#         self.filename = filename
#         self.configurations = {}

#     def read_configurations(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 for line in file:
#                     key, value = line.strip().split('=')
#                     self.configurations[key.strip()] = value.strip()
#             print(f"Successfully loaded configurations from '{self.filename}'.")
#         except FileNotFoundError:
#             print(f"Error: Configuration file '{self.filename}' not found.")
#         except IOError as e:
#             print(f"Error reading configuration file '{self.filename}': {e}")

#     def get_configuration(self, key):
#         return self.configedurations.get(key, None)

#     def display_configurations(self):
#         print(f"Configurations in '{self.filename}':")
#         for key, value in self.configurations.items():
#             print(f"- {key}: {value}")

# ##244. Create a class Database that connects to a database and provides methods to execute queries. 
# #Handle exceptions if the connection fails. 

# class Database:
#     def __init__(self, host, username, password, database):
#         self.host = host
#         self.username = username
#         self.password = password
#         self.database = database
#         self.connection = None

#     def connect(self):
#         try:
#             # Simulate database connection
#             self.connection = True  # Replace with actual database connection code
#             print("Connected to database.")
#         except Exception as e:
#             print(f"Failed to connect to database: {e}")

#     def disconnect(self):
#         if self.connection:
#             # Simulate database disconnection
#             self.connection = None  # Replace with actual disconnection code
#             print("Disconnected from database.")
#         else:
#             print("Not connected to any database.")

#     def execute_query(self, query):
#         try:
#             if not self.connection:
#                 raise Exception("Database not connected.")
#             # Simulate query execution
#             print(f"Executing query: {query}")
#             # Replace with actual query execution code
#         except Exception as e:
#             print(f"Error executing query: {e}")
# ##25
# class Report:
#     def __init__(self, filename):
#         self.filename = filename

#     def generate_report(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 # Simulate report generation
#                 report_data = file.read()
#                 print(f"Report generated successfully from '{self.filename}':")
#                 print(report_data)
#         except FileNotFoundError:
#             print(f"Error: File '{self.filename}' not found.")
#         except IOError as e:
#             print(f"Error reading file '{self.filename}': {e}")
# ##26
# class Ticket:
#     def __init__(self, movie_name, seat_number, price):
#         self.movie_name = movie_name
#         self.seat_number = seat_number
#         self.price = price

#     def display_details(self):
#         print(f"Movie: {self.movie_name}, Seat Number: {self.seat_number}, Price: ${self.price:.2f}")

#     def apply_discount(self, discount):
#         self.price *= (1 - discount / 100

# ##27
# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class ShoppingCart:
#     def __init__(self):
#         self.items = []  # list to store Item objects

#     def add_item(self, item):
#         if isinstance(item, Item):
#             self.items.append(item)
#         else:
#             print("Invalid item object. Please provide an Item instance.")

#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print("Item not found in the shopping cart.")

#     def display_items(self):
#         print("Items in the shopping cart:")
#         for item in self.items:
#             print(f"- {item.name}: ${item.price:.2f}")
# ##28
# class Restaurant:
#     def __init__(self, name):
#         self.name = name
#         self.menu = []  # list to store Item objects

#     def add_item_to_menu(self, item):
#         if isinstance(item, Item):
#             self.menu.append(item)
#         else:
#             print("Invalid item object. Please provide an Item instance.")

#     def remove_item_from_menu(self, item):
#         if item in self.menu:
#             self.menu.remove(item)
#         else:
#             print("Item not found in the menu.")

#     def display_menu(self):
#         print(f"Menu of {self.name}:")
#         for item in self.menu:
#             print(f"- {item.name}: ${item.price:.2f}")
# ##29                                                        
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Flight:
#     def __init__(self, flight_number, destination):
#         self.flight_number = flight_number
#         self.destination = destination
#         self.passengers = []  # list to store Person objects

#     def add_passenger(self, person):
#         if isinstance(person, Person):
#             self.passengers.append(person)
#         else:
#             print("Invalid person object. Please provide a Person instance.")

#     def remove_passenger(self, person):
#         if person in self.passengers:
#             self.passengers.remove(person)
#         else:
#             print("Passenger not found in the flight.")

#     def display_passengers(self):
#         print(f"Passengers on Flight {self.flight_number} to {self.destination}:")
#         for passenger in self.passengers:
#             print(f"- {passenger.name}")
# ##30            
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []  # list to store Room objects

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_occupied:
                    room.is_occupied = True
                    print(f"Room {room_number} booked successfully.")
                else:
                    print(f"Room {room_number} is already occupied.")
                return
        print(f"Room {room_number} not found in {self.name}.")

    def check_out_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_occupied:
                    room.is_occupied = False
                    print(f"Checked out room {room_number}.")
                else:
                    print(f"Room {room_number} is not currently occupied.")
                return
        print(f"Room {room_number} not found in {self.name}.")

    def display_rooms(self):
        print(f"Rooms in {self.name}:")
        for room in self.rooms:
            status = "Occupied" if room.is_occupied else "Available"
            print(f"- Room {room.room_number}: {status}")

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        if room in self.rooms:
            self.rooms.remove(room)
        else:
            print("Room not found in the hotel.")
# # ##31            




