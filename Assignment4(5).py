""" Q:8 How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.
    A:8 Python is an object oriented programming language.
    - Almost everything in Python is an object, with its properties and methods.
    - A Class is like an object constructor, or a "blueprint" for creating objects.
    - in code of python a class is difine at the first of the code or in starting of the code.
    - self is the default parameter of the method."""
class A:
    def add(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        print("the addition is :",self.a + self.b)
a = A()
a.add(5,4)
a.sum()
