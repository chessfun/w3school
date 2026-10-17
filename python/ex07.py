### Python Data Types

from common import print_answer


question = "If x = 5, what is a correct syntax for printing the data type of"
question += "variable x?"


def help_foo(example, answer_str):
    print(question)
    print(example)
    print_answer(answer_str)

print("\tPython Data Types\n")
help_foo("", "print(type(x))")
help_foo("x = 5\nprint(type(x))\n", "int")
help_foo("x = \"Hello World\"\nprint(type(x))\n", "str")
help_foo("x = 20.5\nprint(type(x))\n", "float")
help_foo("x = [\"apple\", \"banana\", \"cherry\"]\nprint(type(x))\n", "list")
help_foo("x = (\"apple\", \"banana\", \"cherry\")\nprint(type(x))\n", "list")
help_foo("x = {\"name\" : \"John\", \"age\" : 36}\nprint(type(x))", "dict")
help_foo("x = True\nprint(type(x))", "bool")


## Python Data Types Code Challenge
# Inside the editor, complete the following steps:
# Create a variable x with the value 5
# Create a variable y with the value 3.14
# Create a variable z with the value "Hello"
# Print the data type of each variable using type()

x, y, z = [5, 3.14, 'Hello']
for a in [x, y, z]:
    print_answer(str(type(a)))
