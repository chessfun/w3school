### Python Classes and Objects


from  common import print_answer


s = '\tWhat is a correct syntax for deleting an object named'
s += 'person in Python?\n'
print(s)
print_answer('del person')


print('Create a class named MyClass:')
s = """
class MyClass:
    x = 5
"""
print_answer(s)


print('Create an object of MyClass called p1:')
s = """class MyClass:
    x = 5

p1 = MyClass()
"""
print_answer(s)


print('Use the p1 object to print the value of x:')
print_answer('print(p1.x)')


## Python Classes/Objects Code Challenge
print('\tPython Classes/Objects Code Challenge\n')
s = """Instructions
1. Inside the editor, complete the following steps:
2. Create a class called Person
3. Add an __init__ method that takes name and age as parameters
4. Add a method called greet that prints "Hello, my name is " followed by the name
5. Create an object p1 of the class with name "John" and age 36
6. Call the greet method on p1
"""
print(s)

# Create a class
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.name)


# Create an object
p1 = Person("John", 36)
# Call the greet method
p1.greet()
del p1
