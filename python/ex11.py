### Python Booleans


from common import print_answer


def help_foo(txt, question, answer):
    print(txt)
    print(question)
    print_answer(answer)
    

print('\tPython Booleans\n')
print('What will be the result of the following syntax:')
print('print(5 > 3)')
print_answer(True)


help_foo('The statement below would print a Boolean value, which one?',
         'print(10 > 9)', True)
help_foo('The statement below would print a Boolean value, which one?',
         'print(10 == 9)', False)
help_foo('The statement below would print a Boolean value, which one?',
         'print(10 < 9)', False)
help_foo('The statement below would print a Boolean value, which one?',
         print(bool("abc")), True)
help_foo('The statement below would print a Boolean value, which one?',
         print(bool(0)), False)


## Python Booleans Code Challenge
print('\tPython Booleans Code Challenge\n')

print('Print the result of 10 > 9')
print_answer(10 > 9)
print('Print the result of 10 == 9')
print_answer(10 == 9)
print('Print the result of bool("Hello")')
print_answer(bool("Hello"))
print('Print the result of bool(0)')
print_answer(bool(0))

