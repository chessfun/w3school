### Python Functions


from common import print_answer


print('\tPython For Loops\n')
print('What is the correct keyword for defining functions in Python?')
print_answer('def')


print('Create a function named my_function.')
s = """def my_function():
    print("Hello from a function")
"""
print_answer(s)


def my_function():
    print("Hello from a function")
print('Execute a function named my_function.')
print_answer('my_function()')


## Python Function Arguments
print('\tPython Function Arguments\n')
print('Consider the following function:')
print('def myfunc(n):\n    print(n)\n')
print('What of the following function call will print "Hello"?')
print_answer('myfunc("Hello")')


print('Inside a function with two parameters, print the first parameter.')
s = """def my_function(fname, lname):
    print(fname)
"""
print_answer(s)


print('Let the function return the x parameter + 5.')
s = """def my_function(x):
    return x + 5
"""
print_answer(s)


## Python *args and **kwargs
print('\tPython *args and **kwargs\n')
print('Keyword arguments are often called, what?')
print_answer('kwargs')


print('If you do not know the number of arguments that will be passed into')
print('your function, there is a prefix you can add in the function ')
print('definition, which prefix?')
s = """def my_function(*kids):
    print("The youngest child is " + kids[2])
"""
print_answer(s)


print('If you do not know the number of keyword arguments that will be ')
print('passed into your function, there is a prefix you can add in the ')
print('function definition, which prefix?')
s = """def my_function(**kid):
    print("His last name is " + kid["lname"])
"""
print_answer(s)


## Python Scope
print('\tPython Scope\n')
print('Consider the following code:')
s = """x = 300
def myfunc():
    x = 200
myfunc()
print(x)
"""
print(s)
print('What will be the printed result?')
print_answer(300)


print('Consider the following code:')
s = """x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)
"""
print_answer(200)


print('Which statement keyword can be used for variables inside nested ')
print('function?')
print_answer('nonlocal')


## Python Decorators
## I think it's some kind of shit
print('Python Decorators?')
print('What is the main purpose of a decorator in Python?')
s = 'To wrap a function and extend/modify its behavior without changing'
s += 'its source'
print_answer(s)


print('What does functools.wraps do when used inside a decorator?')
s = "It preserves the original function's metadata (name, docstring, signature)"
print_answer(s)


print('What is the output of the following code?')
s = """def upper(f):
    def w():
        return f().upper()
    return w

def exclaim(f):
    def w():
        return f() + "!"
    return w

@upper
@exclaim
def say():
    return "hi"

print(say())
"""
print(s)
print_answer('HI!')


## Python Lambda
print('\tPython Lambda\n')
print('What will be the result of the following code:')
print('x = lambda a, b : a - b\nprint(x(5, 3))\n')
print_answer(2)


print('True or False: Lambda functions can take multiple arguments.')
print_answer(True)


print('True or False: Lambda functions can have multiple expressions.')
print_answer(False)


print('Create a lambda function that takes one parameter (a) and returns it.')
print_answer('x = lambda a: a')


## Python Functions Code Challenge
print('\tPython Functions Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a function called greet
2. Add a parameter called name to the function
3. Inside the function, print "Hello, " followed by the name parameter
4. Call the function with the argument "Emil"
"""
print(s)
# Create the greet function
def greet(name):
	print("Hello, " + name)
# Call greet
greet("Emil")
