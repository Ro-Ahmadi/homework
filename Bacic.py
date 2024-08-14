
# 1. Create a class called Person with attributes name and age. Create an object of the class and print 
# its attributes.


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# Amin=person("Amin",25)
# print(Amin.age())
# print(Amin.name())

# 2. Add a method called greet to the Person class that prints a greeting message including the 
# person's name.
# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         return F"({self.name},{"Hello How are you??"})"
# Amin=person("Amin")
# print(Amin.greet())

# 3. Create a class called Car with attributes make, model, and year. Include a method to print out 
# the car's details.

# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

#     def out_of_car_detels(self):
#         return F"({"the car Deteals are"}  {self.make},{self.model},{self.year})"

# truck=Car("Tesla","BmW",2024)
# print(truck.out_of_car_detels())

# 4. Create a class Circle with a method to compute the area. Initialize the class with the radius?


# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def compute_area(self):
#         return math.pi * (self.radius ** 2)
# circle=Circle(5)
# print(circle.compute_area())       


# 5. Create a class Rectangle with methods to compute the area and perimeter. Initialize the class 
# with the length and width.

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self):
        return (self.width*self.length)
    def perimeter(self):
        return 2*(self.width+self.length)
    
rectangle=Rectangle(5,3)
print("the area is ",rectangle.area())
print("the perimeter  is ",rectangle.perimeter())
