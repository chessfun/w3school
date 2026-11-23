### Python Modules


from common import print_answer


print('\tPython Modules\n')
print('True or False. A module can only contain one function or object.')
print_answer(False)


print('What is the correct syntax to import a module named "mymodule"?')
print_answer('import mymodule')


print('If you want to refer to a module by using a different name, you can ')
print('create an alias. What is the correct syntax for creating an alias ')
print('for a module?')
print_answer('import mymodule as mx')


print('What is the correct syntax of printing all variables and function ')
print('names of the "mymodule" module?')
print_answer('print(dir(mymodule))')


print('What is the correct syntax of importing only the person1 dictionary of')
print('the "mymodule" module?')
print_answer('from mymodule import person1')


## Python Modules Code Challenge
print('\tPython Modules Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Import the platform module
2. Print the system platform using platform.system()
"""
print(s)
# Import the platform module
import platform
# Print the system platform
print(platform.system())
