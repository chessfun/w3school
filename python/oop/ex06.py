### Python Magic Methods


from common import print_answer


print('\tPython Magic Methods\n')
print('Which of these is a magic method?')
print_answer('__init__()')


print("Why are __init__() and __str__() called 'dunder methods'?")
print_answer('Because they start and end with double underscores')


print('How do you call a magic method like __str__()?')
print_answer("You don't - Python calls it automatically")


## The __str__() Method
print('\tThe __str__() Method\n')
print('What does __str__() control?')
print_answer('What is returned when the object is printed')


print('Without a __str__() method, what does print(obj) show?')
print_answer("The object's memory address")


print('What must a __str__() method return?')
print_answer('A string')


## Python __repr__() Method
print('\tPython __repr__() Method\n')
print('What is __repr__() mainly meant for?')
print_answer('A technical representation, meant for developers')


s = 'If a class has no __str__() method,'
s += 'which method does print() fall back to?'
print(s)
print_answer('__repr__()')


print('Which built-in function calls __repr__() directly?')
print_answer('repr()')


## Python __eq__() Method
print('\tPython __eq__() Method\n')
s = 'By default (without __eq__()), what does p1 == p2 check'
s += ' for two custom objects?'
print(s)
print_answer('If they are the exact same object in memory')


print('What does __eq__() let you customize?')
print_answer('How two objects are compared with ==')


print('What is the second parameter of __eq__(self, other) used for?')
print_answer('It represents the other object being compared to')


## Python __add__() Method
print('\tPython __add__() Method\n')
s = 'Which magic method lets you customize what happens when you use the + '
s += 'operator on your own objects?'
print(s)
print_answer('__add__()')


s = 'What is this pattern called, where an operator is given custom behavior'
s += ' for your own class?'
print(s)
print_answer('Operator overloading')


s = 'Without __add__(), what happens if you try p1 + p2 on two custom objects?'
print(s)
print_answer('A TypeError is raised')


## Python __len__() Method
print('\tPython __len__() Method\n')
print('Which built-in function calls __len__()?')
print_answer('len()')


print('What must __len__() return?')
print_answer('A number')


s = 'Without __len__(), what happens if you call len(obj) on a custom object?'
print(s)
print_answer('It raises a TypeError')


## Python __lt__() Method
print('\tPython __lt__() Method\n')
print('Which operator does __lt__() control?')
print_answer('<')


print('Besides the < operator, what else can use __lt__()?')
print_answer('sorted()')


print('What will this code print?')
s = """
class Person:
    def __init__(self, age):
        self.age = age
    def __lt__(self, other):
        return self.age < other.age

p1 = Person(22)
p2 = Person(19)
print(p1 < p2)
"""
print(s)
print_answer(False)


## Python __contains__() Method
print('\tPython __contains__() Method\n')
print('Which operator does __contains__() control?')
print_answer('in')


print('What must __contains__() return?')
print_answer('A boolean (True or False)')


print('What will this code print?')
s = """
class Company:
    def __init__(self, employees):
        self.employees = employees
    def __contains__(self, name):
        return name in self.employees

c1 = Company(['Emil', 'Tobias'])
print('Tobias' in c1)
"""
print(s)
print_answer(True)


## Python __call__() Method
print('\tPython __call__() Method\n')
print('What does __call__() let you do?')
print_answer('Call an object like a function, using object()')


print('What will this code print?')
s = """
class Counter:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c())
print(c())
"""
print(s)
print_answer('1\n2\n')


print('Why is a callable object sometimes more useful than a plain function?')
s = "It can remember state between calls, a function can't do that on its own"
print_answer(s)


## Python Magic Methods Code Challenge
s = """Inside the editor, complete the following steps:
1. Create a class called Point
2. Add an __init__ method with x and y, and store them as properties
3. Add a __repr__ method that returns f"Point({x}, {y})"
4. Create an object p1 with x 2 and y 3
5. Print p1
"""
print(s)
# Create the Point class
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return f"Point({self.x}, {self.y})"
# Create an object
p1 = Point(2, 3)
# Print it
print(p1)
