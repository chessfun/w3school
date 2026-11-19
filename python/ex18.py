### Python Match

from common import print_answer


print('\tPython Match\n')
print('Which character can be used as a default case value in a match ')
print('statement?')
print_answer('_')


print('Insert the correct keywords to make a match statement:')
s = """day = 4
match day:
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Looking forward to the weekend')
"""
print(s)


print('Which operator is used as an OR operator in the case evaluation?')
print_answer('|')


## Python Match Code Challenge
print('Python Match Code Challenge')
s = """Inside the editor, complete the following steps:
1. Create a variable day with the value 3
2. Use a match statement to check the value of day
3. Add a case 3 that prints 'Wednesday'
4. Add a wildcard case _ that prints 'Other day'
"""
print(s)
# Create variable day
day = 3
# Use match statement
match day:
    case 3:
        print("Wednesday")
    case _:
        print("Other day")
