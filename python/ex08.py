### Python Numbers


from common import print_answer


def help_foo(question, example, answer):
    print(f'Insert the correct syntax to convert x into a {question}.', question)
    print(example)
    print_answer(answer)
    

print('Python Numbers')
print('Which is NOT a legal numeric data type in Python:')
print_answer('long')


help_foo('floating point number', 'x = 5\nx = ____(x)\n', 'float')
help_foo('integer', 'x = 5.5\nx = ____(x)\n', 'int')
help_foo('complex', 'x = 5\nx = ____(x)\n', 'complex')


## Code challenge


print('Code challenge')
"""Inside the editor, complete the following steps:
Create a variable x and assign it the integer 5
Create a variable y and assign it the float 3.14
Create a variable z and assign it the complex number 2+3j
Print the type of each variable using type()"""


x, y, z = 5, 3.14, 2 + 3j

# Print the types
for a in [x, y, z]:
    print(type(a))


