### Python None


from common import print_answer


print('\tPython None\n')
print('What is the data type of the value None?')
print_answer('NoneType')


print('How should you compare a variable to None?')
print_answer('x is None')


print('What does a function without a return statement return?')
print_answer(None)


## Python None Code Challenge
print('\tPython None Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a variable x and assign it the value None
2. Use if to check if x is None, and if so, print "x is None"
"""
print(s)
# Assign None to x
x = None
# Check if x is None
if x is None:
	print("x is None")
