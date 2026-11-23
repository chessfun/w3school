### Python Datetime


from common import print_answer


print('\tPython Datetime\n')
print('Consider the following code:')
print('import datetime\nx = datetime.datetime\n')
print('Which syntax will print the current date?')
print_answer('print(x.now())')


print('Consider the following code:')
print('import datetime\nx = datetime.datetime\n')
print('Which syntax will print the name of the weekday?')
print_answer("print(x.strftime('%A'))")


print('When formatting date objects into readable strings, which syntax is ')
print('used to return the month name, full version?')
print_answer("print(x.strftime('%B'))")


print('Consider the following code:')
print("import datetime\nx = datetime.datetime(2024, 8, 20)\n")
print("print(x.strftime('%d'))")
print('What will be the printed result?')
print_answer(20)


## Python Dates Code Challenge
print('\tPython Dates Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Import the datetime module
2. Store the current date and time in a variable called x
3. Print the year from x
"""
print(s)
# Import the datetime module
import datetime
# Store the current date and time in x
x = datetime.datetime.now()
# Print the year
print(x.strftime("%Y"))
