# What are oops concepts? Is multiple inheritance supported in java
'''
Ans. oops means object oriented programming. it includes an encapsulation, abstraction, inheritance, polymorphism etc..
    it is an important part for all programing languages.
    multiple inheritance is not supported in java but in case of interface it is supported in some advanced situation.
'''

# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
'''
Ans. class is a component of oops concept. class is defined by "class" keyword. by defining a class you can perform oops
concept thats why it is important.
    self: self is a by default parameter of any function.
'''

class A:
    def a(self):
        print("hello my name is devarth")
a1=A()
a1.a()
print("================================================================================")
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width
    
rectangle1 = Rectangle(5, 10)
area1 = rectangle1.compute_area()
print("Area of rectangle1:", area1)
rectangle2 = Rectangle(7, 3)
area2 = rectangle2.compute_area()
print("Area of rectangle2:", area2)
print("================================================================================")
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def compute_area(self):
        return math.pi * self.radius**2
    def compute_perimeter(self):
        return 2 * math.pi * self.radius
circle1 = Circle(5)
area1 = circle1.compute_area()
print("Area of circle1:", area1)
perimeter1 = circle1.compute_perimeter()
print("Perimeter of circle1:", perimeter1)
circle2 = Circle(3)
area2 = circle2.compute_area()
print("Area of circle2:", area2)
perimeter2 = circle2.compute_perimeter()
print("Perimeter of circle2:", perimeter2)
print("================================================================================")

# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def compute_area(self):
        return math.pi * self.radius**2
    def compute_perimeter(self):
        return 2 * math.pi * self.radius
circle1 = Circle(5)
area1 = circle1.compute_area()
print("Area of circle1:", area1)
perimeter1 = circle1.compute_perimeter()
print("Perimeter of circle1:", perimeter1)
circle2 = Circle(3)
area2 = circle2.compute_area()
print("Area of circle2:", area2)
perimeter2 = circle2.compute_perimeter()
print("Perimeter of circle2:", perimeter2)
print("================================================================================")

# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 
'''
Ans. Inheritance in Python allows a class (known as a subclass or derived class) to inherit attributes and behaviors
from another class (known as a superclass or base class).
init: init method is a super method and it also knows a constructor method. by use of init method you can take data or
value from another methods.
'''
class A:
    def a(self):
        print("A class")
class B(A):
    def b(self):
        print("B class")
b1 = B()
b1.a()
b1.b()
print("================================================================================")

# What is Instantiation in terms of OOP terminology?
'''
Ans: In object-oriented programming (OOP) terminology, instantiation refers to the process of creating an instance or object
of a class.When you instantiate a class, you are essentially creating a specific, unique object based on that class's
blueprint. The newly created object is an instance of the class and has its own set of attributes and can perform
actions defined by the methods of the class.
'''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    
my_car = Car("Toyota", "Camry")
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print("================================================================================")

# What is used to check whether an object o is an instance of class A?
'''

In most object-oriented programming languages, including Python, you can use the isinstance() function to check whether
an object o is an instance of a specific class A. This function returns True if the object is an instance of the
specified class, and False otherwise.
'''
class A:
    pass
class B:
    pass

o = B()

if isinstance(o, A):
    print("o is an instance of class A")
else:
    print("o is not an instance of class A.")
print("================================================================================")

# What relationship is appropriate for Course and Faculty? 
'''
single inheritance is used for course and faculty.
'''
print("================================================================================")

# What relationship is appropriate for Student and Person?
'''
multilevel inheritance is used for student and person.
'''













