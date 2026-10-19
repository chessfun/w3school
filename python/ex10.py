### Python Strings


from common import print_answer


print('\tPython Strings\n')
print('What will be the result of the following code:')
print("x = 'Welcome'\nprint(x[3])")
print_answer('c')


print('Use the len function to print the length of the string.')
print('x = "Hello World"\nprint(_____)')
print_answer('len(x)')


print('Get the first character of the string txt.')
print('txt = "Hello World"\nx = ______')
print_answer('x = txt[0]')


print('Insert the correct keyword to check if the word "free" is present in ')
print('the text:')
s = """txt = 'The best things in life are free!'
if 'free' ______ txt:
    print('Yes, free is present in the text.')"""
print(s)
print_answer('in')


## Python - Slicing Strings
print('\tPython - Slicing Strings\n')
print('What will be the result of the following code:')
print("x = 'Welcome'\nprint(x[3:5])")
print_answer('co')


print('Get the characters from index 2 to index 4 (llo).')
print('txt = "Hello World"\nx = ______')
print_answer('txt[2:5]')


print('What will be the result of the following code:')
print("x = 'Welcome'\nprint(x[3:])")
print_answer('come')


## Python - Modify Strings
print('\tPython - Modify Strings\n')
print('What is a correct syntax to print a string in upper case letters?')
print_answer("'Welcome'.upper()")


print('Return the string without any whitespace at the beginning or the end.')
print('txt = " Hello World "\nx = ______')
print_answer('txt.strip()')


print('Convert the value of txt to upper case.')
print('txt = "Hello World"\ntxt = ___________')
print_answer('txt.upper()')


print('Convert the value of txt to lower case.')
print('txt = "Hello World"\ntxt = ___________')
print_answer('txt.lower()')


print('Replace the character H with a J.')
print('txt = "Hello World"\ntxt = txt.______(___,___)')
print_answer("txt.replace('H', 'J'")


## Python - String Concatenation
print('\tPython - String Concatenation\n')
print('What is a correct syntax to merge variable x and y into variable z?')
print_answer('z = x + y')


print('What will be the result of the following code:')
print("x = 'Welcome'\ny = 'Coders'\nprint(x + y)")
print_answer('WelcomeCoders')


print('Consider this code:')
print("a = 'Join'\nb = 'the'\nc = 'party'")
print("What is a correct syntax to print 'Join the party'?")
print_answer("print(a + ' ' + b + ' ' + c)")


## Python - Format - Strings
print('\tPython - Format - Strings\n')
print("If x = 9, what is a correct syntax to print 'The price is 9.00 dollars'?")
print_answer("print(f'The price is {x:.2f} dollars')")


print('Insert the correct syntax to add a placeholder for the age parameter.')
s = """age = 36
txt = f"My name is John, and I am _____"
print(txt)"""
print(s)
print_answer('{age}')


print('What will be the result of the following code:')
print("print(f'The price is {2 + 3} dollars')")
print_answer('The price is 5 dollars')


## Python Strings Code Challenge
print('\tPython Strings Code Challenge\n')
# Create the variable
print('Create the variable')
txt = "Hello, World!"
# Print characters from index 2 to 5
print('Print characters from index 2 to 5')
print(txt[2:5])
# Print in upper case
print('Print in upper case')
print(txt.upper())
# Create the name variable
print('Create the name variable')
name = "Python"
# Print using an f-string
print('Print using an f-string')
print(f"I love {name}")
