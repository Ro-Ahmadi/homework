           
# advance class 


# 16. Create a class Library with attributes name and books (a list of Book objects). Provide methods 
# to add and remove books.



# class Book:
#     def __init__(self,book_name):
#         self.book_name=book_name

#     def __str__(self):
#         return f"Book_name is:{self.book_name}"

# class Library:
#     def __init__(self, name):
#         self.name = name            # Name of the library
#         self.books = []             # List of Book objects

#     def add_book(self, book):
#         """Add a book to the library."""
#         if isinstance(book, Book):
#             self.books.append(book)
#             print(f"Added book: {book}")
#         else:
#             print("Only objects of type Book can be added.")

#     def remove_book(self, book_name):
#         """Remove a book from the library by title."""
#         for book in self.books:
#             if book.book_name == book_name:
#                 self.books.remove(book)
#                 print(f"Removed book: {book}")
#                 return
#         print(f"No book found with title '{title}'.")

#     def display_books(self):
#         """Display all books in the library."""
#         if self.books:
#             print(f"Books in {self.name}:")
#             for book in self.books:
#                 print(book)
#         # else:
#         #     print(f"No books available in {self.name}.")

# # Example usage:
# library = Library("Afghan")  # Create a library

#  # Create some Book objects
# book1 = Book("python programing")
# book2=Book("java")

# # Add books to the library
# library.add_book(book1)
# library.add_book(book2)
# # Display all books
# library.display_books()

# library.remove_book("python programing")

# # # Display all books after removal 
# # library.display_books()

############################################################################################################################
 


# 17. Create a class School with attributes name and students (a list of Student objects). Provide 
# methods to add and remove students.

class Student:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f"Name: {self.name}"

class School:  
    def __init__(self, school_name):
        self.school_name = school_name                # Name of the school
        self.students = []              # List of Student objects

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"Added student: {student}")

    def remove_student(self, name):
       
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Removed student: {student}")
            

    def display_students(self):
        
        if self.students:
            print(f"Students in {self.school_name}:")
            for student in self.students:
                print(student)
       


school = School("Noor High school") 

student1 = Student("Ali")
student2 = Student("Ahmad")
student3 = Student("salim")


school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.display_students()

school.remove_student("Ali")

school.display_students()


# 18. Create a class Team with attributes name and members (a list of Person objects). Provide 
# methods to add and remove members.




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Team:
    def __init__(self, name):
        self.name = name                # Name of the team
        self.members = []              # List of Person objects

    def add_member(self, person):
        """Add a member to the team."""
        if isinstance(person, Person):
            self.members.append(person)
            print(f"Added member: {person}")
        else:
            print("Only objects of type Person can be added.")

    def remove_member(self, name):
        """Remove a member from the team by name."""
        for person in self.members:
            if person.name == name:
                self.members.remove(person)
                print(f"Removed member: {person}")
                return
        print(f"No member found with name '{name}'.")

    def display_members(self):
        """Display all members of the team."""
        if self.members:
            print(f"Members of {self.name}:")
            for person in self.members:
                print(person)
        else:
            print(f"No members available in {self.name}.")

# Example usage:
team = Team("Developers")  # Create a team

# Create some Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# Add members to the team
team.add_member(person1)
team.add_member(person2)
team.add_member(person3)

# Display all members
team.display_members()

# Remove a member
team.remove_member("Bob")

# Display all members after removal
team.display_members()







# 19. Create a class Company with attributes name and employees (a list of Employee objects). 
# Provide methods to add and remove employees.






# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def __str__(self):
#         return F"Name:{self.name},Age:{self.age},Salary:{self.salary}"
    

# class Company:
#     def __init__(self,company_name):
#         self.company_name=company_name
#         self.employees=[]
#     def add_employee(self,employee):
#         if isinstance(employee,Employee):
#             self.employees.append(employee)
#             print(f"Added Employe is : {employee}")
#         else:
#             print("only object Employee can add")
#     def remove_employee(self,name):
#         for employee in self.employees:
#             if employee.name==name: 
#                 self.employees.remove(employee)
#                 print(f"Removed employee is : {employee}")


#     def disply_details(self):
#         if self.employees:
#             print(f"Employees of :{self.company_name}")
#             for employee in self.employees:
#                 print(employee)




# Google=Company("Google")
# employee1=Employee("salim",22,999999)
# employee2=Employee("masom",66,55555)
# employee3=Employee("shahar",55,123445)

# Google.add_employee(employee1)
# Google.add_employee(employee2)
# Google.add_employee(employee3)

# Google.remove_employee("salim")

# Google.disply_details()





# 20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods 
# to add and remove animals


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

class Zoo:
    def __init__(self, name):
        self.name = name                # Name of the zoo
        self.animals = []              # List of Animal objects

    def add_animal(self, animal):
        """Add an animal to the zoo."""
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Added animal: {animal}")
        else:
            print("Only objects of type Animal can be added.")

    def remove_animal(self, name):
        """Remove an animal from the zoo by name."""
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"Removed animal: {animal}")
                return
        print(f"No animal found with name '{name}'.")

    def display_animals(self):
        """Display all animals in the zoo."""
        if self.animals:
            print(f"Animals in {self.name}:")
            for animal in self.animals:
                print(animal)
        else:
            print(f"No animals available in {self.name}.")

# Example usage:
zoo = Zoo("Wildlife Safari")  # Create a zoo

# Create some Animal objects
animal1 = Animal("Lion", "Panthera leo", 5)
animal2 = Animal("Elephant", "Loxodonta africana", 10)
animal3 = Animal("Giraffe", "Giraffa camelopardalis", 7)

# Add animals to the zoo
zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)

# Display all animals
zoo.display_animals()

# Remove an animal
zoo.remove_animal("Elephant")

# Display all animals after removal
zoo.display_animals()
























