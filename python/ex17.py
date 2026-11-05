### Python if...Else


from common import print_answer


## If Statement
print('\tIf Statement\n')
ask = 'What does an if statement evaluate?'
print(ask)
print_answer('A condition that results in True or False')


ask = 'What will happen if the condition in an if statement is False?'
print(ask)
print_answer('The code block will be skipped')


ask = 'What is required for proper if statement syntax in Python?'
print(ask)
print_answer('Indentation for the code block')


ask = 'Print "Hello World" if a is greater than b.'
print(ask)
s = """a = 50
b = 10
if a > b:
    print("Hello World")"""
print_answer(s)


ask = 'Print "Hello World" if a is NOT equal to b.'
print(ask)
s = """a = 50
b = 10
if a != b:
    print("Hello World")"""
print_answer(s)


ask = 'Complete the code block, print "YES" if 5 is larger than 2.\n'
ask += 'Hint: remember the indentation.'
print(ask)
s = """if 5 > 2:
    print("YES")"""
print_answer(s)


## Python Elif
print('\tPython Elif\n')
print('What does the elif keyword mean?')
print_answer('If the previous conditions were not true, try this condition')


print('What happens when Python finds a true condition in an if-elif chain?')
print_answer('It executes that block and skips the rest')


print('How many elif statements can you have?')
print_answer('As many as you need')


print('Print "1" if a is equal to b, print "2" if a is greater than b, ')
print('otherwise print "3".')
s = """a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")"""
print_answer(s)


## Python Else
print('\tPython Else\n')
print('When does the else statement execute?')
print_answer('When the if condition (and any elif conditions) are False')


print('Can you have an else statement without an elif?')
print_answer('Yes')


print('Where must the else statement be placed?')
print_answer('Last in the if-elif-else chain')


print('What will be the result of the following code:')
s = """x = 5
y = 8
if x > y:
    print('Hello')
else:
    print('Welcome')"""
print(s)
print_answer('Welcome')


print('Print "Yes" if a is equal to b, otherwise print "No".')
s = """a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")"""
print_answer(s)


## Python Shorthand If
print('\tPython Shorthand If\n')
print('What is another name for the one-line if/else statement?')
print_answer('Conditional expression (ternary operator)')


print('What is the correct syntax for a ternary operator?')
print_answer('value_if_true if condition else value_if_false')


print('Use the correct one line short hand syntax to print "YES" if a is ')
print('equal to b, otherwise print("NO").')
s = """a = 2
b = 5
print('YES') if a == b else print('NO')"""
print_answer(s)


## Python Logical Operators
print('\tPython Logical Operators\n')
print('What does the and operator require?')
print_answer('Both conditions must be True')


print('What does the or operator require?')
print_answer('At least one condition must be True')


print('What does the not operator do?')
print_answer('Reverses the boolean value')


print('Print "Hello" if a is equal to b, and c is equal to d.')
s = """if a == b and c == d:
    print("Hello")"""
print_anser(s)


print('Print "Hello" if a is equal to b, or if c is equal to d.')
s = """if a == b or c == d:
    print("Hello")"""
print_anser(s)


print('Use an if statement to print "YES" if either a or b is equal to c.')
s = """a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")"""
print_anser(s)


## Python Nested If
print('\tPython Nested If\n')
print('What is a nested if statement?')
print_answer('An if statement inside another if statement')


print('When does an inner if statement run?')
print_answer('Only if the outer condition is True')


print('Can nested if statements be replaced with logical operators?')
print_answer('Sometimes, depending on the logic')


## Python Pass Statement
print('\tPython Pass Statement\n')
print_answer("It's a null operation - nothing happens")


print('Why is the pass statement useful?')
print_answer('To serve as a placeholder for future code')


print('Can you use only a comment inside an if statement without pass?')
print_answer('No, it will cause an error')
