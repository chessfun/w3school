### Python Class Methods


from common import print_answer


print('\tPython Class Methods\n')
print('Insert the missing parts to make the code return: John(36):')
s = """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person('John', 36)
print(p1)
"""
print_answer(s)


print('What is the first parameter that all class methods must have?')
print_answer('self')


print('What will be the result of the following code:')
s = """
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))
"""
print(s)
print_answer(8)


print('When the class object is represented as a string, there is a method ')
print('that controls what should be returned, which one?')
print_answer('__str__()')


print('What is the purpose of the __str__() method?')
print_answer('To control what is returned when the object is printed')


## Python Class Methods Code Challenge
print('\tPython Class Methods Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a class called Rectangle
2. Add an __init__ method with width and height, and store them as properties
3. Add a method called area that returns the width multiplied by the height
4. Create an object r1 with width 5 and height 3
5. Print the area of r1
"""
print(s)

# Create the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

# Create an object
r1 = Rectangle(5, 3)
# Print the area
print(r1.area())
