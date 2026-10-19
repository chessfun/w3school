### Python Operators


from common import print_answer


print('\tPython Operators\n')
print('What is the result of 15 % 4?')
print_answer(3)


print('Which operator is used for exponentiation in Python?')
print_answer('**')


print('What is the difference between / and // operators?')
print_answer('/ returns a float, // returns an integer')


print('Multiply 10 with 5, and print the result.')
print_answer('print(10 * 5)')


print('Divide 10 by 2, and print the result.')
print_answer('print(10 / 2)')


## Python Assignment Operators
print('\tPython Assignment Operators\n')
print('What will be the value of x after this code?')
print('x = 10\nx += 5')
print_answer(15)


print('Which operator assigns a value to a variable AND uses it in an')
print('expression?')
print_answer(':=')


print('What will be the result of the following syntax:')
print('x = 5\nx += 3\nprint(x)')
print_answer(8)


print('What does x *= 3 mean?')
print_answer('x = x * 3')


## Python Comparison Operators
print('\tPython Comparison Operators\n')
print('What is the result of 5 == 5?')
print_answer(True)


print('Which operator checks if two values are NOT equal?')
print_answer('!=')


print('What does the expression 1 < x < 10 check?')
print_answer('If x is between 1 and 10')


print('Use the correct comparison operator to check if 5 is not equal to 10.')
print_answer('!=')


## Python Logical Operators
print('\tPython Logical Operators\n')
print('What is the result of 5 < 7 and 5 > 7?')
print_answer(False)


print('What is the result of 5 < 7 or 5 > 7?')
print_answer(True)


print('What does the not operator do?')
print_answer('Reverses the boolean value')


print('Use the correct logical operator to check if at least one of two ')
print('statements is True.')
print('if 5 == 10 ___  4 == 4:')
print_answer('or')


## Python Identity Operators
print('\tPython Identity Operators\n')
print('What does the is operator check?')
print_answer('If two variables point to the same object')


print('What is the result of [1,2] is [1,2]?')
print_answer(False)


print('What is the difference between is and ==?')
print_answer('is checks identity, == checks value')


## Python Membership Operators
print('\tPython Membership Operators\n')
print('What does the in operator do?')
print_answer('Checks if a value exists in a sequence')


print("What is the result of 'a' in 'apple'?")
print_answer(True)


print('Are membership operators case-sensitive when used with strings?')
print_answer(True)


print('Use the correct membership operator to check if "apple" is present in ')
print('the fruits object.')
print('fruits = ["apple", "banana"]')
print_answer('if "apple" in fruits:')


## Python Bitwise Operators
print('What is the result of 0b110 & 0b011?')
print_answer('0b010')


print('What is the result of 0b110 | 0b011?')
print_answer('0b111')


print('What does the XOR (^) operator return when both bits are 1?')
print_answer(0)


## Python Operator Precedence
print('\tPython Operator Precedence\n')
print('What is the result of 2 + 3 * 4?')
print_answer(14)


print('Which operator has higher precedence? [+, *]')
print_answer('* (multiplication)')


print('What is the result of 10 - 5 + 3?')
print_answer(8)


## Python Operators Code Challenge
print('Python Operators Code Challenge')
print('Create variables a = 15, b = 4')
a, b = 15, 4
print('Print a modulus b')
print(a % b)
print('Print a floor division b')
print(a // b)
print('Print a power b')
print(a ** b)
print('Add 10 to a')
a += 10
print('a += 10')
