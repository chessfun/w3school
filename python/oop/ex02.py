### Python __init__() Method


from  common import print_answer


print('\tPython __init__() Method\n')
print('What is the purpose of the __init__() method in Python classes?')
print_answer('To assign initial values to object properties')

print('What will be the result of the following code: (see comment beelow)')
# class Person:
#   def __init__(self, name, age=18):
#     self.name = name
#     self.age = age

# p1 = Person("Emil")
# print(p1.age)
print_answer(18)


print('When is the __init__() method called?')
print_answer('Automatically when creating a new object')


print('What is the correct syntax to assign a "init" method to a class?')
s = """class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age
"""
print_answer(s)


## Python __init__ Method Code Challenge
print('\tPython __init__ Method Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a class called Dog
2. Add an __init__ method with parameters name and age, and store them as properties using self
3. Add a method called bark that prints the dog's name followed by " says Woof!"
4. Create an object d1 of the Dog class with name "Buddy" and age 3
5. Call the bark method on d1
"""
print(s)
# Create the Dog class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def bark(self):
    print(" says Woof!")
# Create an object
d1 = Dog("Buddy", 3)
# Call the bark method
d1.bark()
del d1
