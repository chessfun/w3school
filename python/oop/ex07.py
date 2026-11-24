### Python Inheritance


from common import print_answer


print('\tPython Inheritance\n')
s = 'What is the correct keyword to use inside an empty class, '
print(s + 'to avoid getting an error?')
print_answer('pass')


s = 'What is the correct syntax to create a class named Student that will '
s += 'inherit properties and methods from a class named Person?'
print(s)
print_answer('class Student(Person):')


s = 'We have used the Student class to create an object named x. What is the '
s += 'correct syntax to execute the printname method of the object x?'
print(s)
s = """
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
"""
print(s)
print_answer('x.printname()')


print('How do you create a child class that inherits from a parent class?')
print_answer('class Child(Parent):')


s = "Which function allows a child class to inherit all methods and properties"
s += "from its parent without using the parent's name?"
print_answer('super()')


## Python Inheritance Code Challenge
print('Python Inheritance Code Challenge')
s = """Inside the editor, complete the following steps:
1. Create a parent class Animal with an __init__ that takes name
2. Add a method speak that prints the name
3. Create a child class Dog that inherits from Animal
4. Create an object d1 = Dog("Rex")
5. Call d1.speak()
"""
# Create the Animal class
class Animal:
	def __init__(self, name):
		self.name = name
	def speak(self):
		print(self.name)
# Create the Dog class (inherits from Animal)
class Dog(Animal):
	pass
# Create an object
d1 = Dog("Rex")
# Call the speak method
d1.speak()
