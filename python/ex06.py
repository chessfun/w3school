### Python Variables

from common import print_answer

print("\tPyton Variables\n")
print("What is a correct way to declare a Python variable?")
print_answer("x = 5")


print("You can declare string variables with single or double quotes.")
print_answer(True)


print("You can declare string variables with single or double quotes.")
print("""a = 5
# is the same as
A = 5""")
print_answer(False)


print("Select the correct functions to print the data type of a variable:")
print_answer("print(type(myvar))")


## Python - Variable Names

print("\tPython - Variable Names\n")
print("Which is NOT a legal variable name?")
print_answer("my-var = 20")


print("Create a variable named carname and assign the value Volvo to it.")
print_answer("carname = 'Volvo'")


print('Create a variable named x and assign the value 50 to it.')
print_answer("x = 50")


## Python Variables - Assign Multiple Values


print("\tPython Variables - Assign Multiple Values\n")
print("What is a correct syntax to add the value 'Hello World'")
print(", to 3 variables in one statement?")
print_answer("x = y = z = 'Hello World'")


print("Insert the correct syntax to assign values")
print("to multiple variables in one line:")
print_answer("""x, y, z = \"Orange\", \"Banana\", \"Cherry\"""")


print("Consider the following code:")
print("\tfruits = ['apple', 'banana', 'cherry']")
print("\ta, b, c = fruits")
print("print(a)")
print_answer("apple")


## Python - Output Variables


print("\tPython - Output Variables\n")
print("Consider the following code:")
print("print('Hello', 'World')")
print("What will be the printed result?")
print_answer("Hello World")


print("Consider the following code:")
print("""a = 'Hello'
b = 'World'
print(a + b)""")
print_answer("HelloWorld")


print("Consider the following code:")
print("""a = 4
b = 5
print(a + b)""")
print("What will be the printed result?")
print_answer(9)


## Python - Global Variables


print("\tPython - Global Variables\n")
print("Consider the following code:")
print("""x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)""")
print("What will be the printed result?")
print_answer("Python is awesome")


print("Insert the correct keyword to make the variable x belong to", end=" ")
print("the global scope.")
print_answer("""def myfunc():\n\tglobal x\n\tx = "fantastic"\n""")


print("Consider the following code:")
print("""x = 'awesome'
def myfunc():
    global x
    x = 'fantastic'
myfunc()
print('Python is ' + x)""")
print("What will be the printed result?")
print_answer("Python is fantastic")


## Python - Variable Exercises


print("\tPython - Variable Exercises\n")
print("If x = 5, what is a correct syntax for printing the data type of the")
print("variable x?")
print_answer("print(type(x))")


def help_foo(src, answer):
    print("The following code example would print the data type of x, what")
    print(" data type would that be?")
    print(src)
    print_answer(answer)


help_foo("x = 5\nprint(type(x))\n", "int")
help_foo("x = \"Hello World\"\nprint(type(x))\n", "str")
help_foo("x = 20.5\nprint(type(x))\n", "float")
help_foo("x = [\"apple\", \"banana\", \"cherry\"]\nprint(type(x))\n", "list")
help_foo("x = (\"apple\", \"banana\", \"cherry\")\nprint(type(x))", "tuple")
help_foo("x = {\"name\" : \"John\", \"age\" : 36}\nprint(type(x))", "dict")
help_foo("x = True\nprint(type(x))", "bool")


## Python Variables Code Challenge


print("Python Variables Code Challenge")
print("Create variable x with value 5")
print("Create variable y with value \"John\"")
print("Print the type of x")
print_answer("x = 5\ny = \"John\"\nprint(type(x))")
