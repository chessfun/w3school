
### Python Tuples


from common import print_answer


print('\tPython Tuples\n')
print('Which one of these is a tuple?')
print_answer("thistuple = ('apple', 'banana', 'cherry')")


print('Use the correct syntax to print the number of items in the fruits')
print('tuple.\n' + 'fruits = ("apple", "banana", "cherry")')
print_answer('print(len(fruits))')


print('Tuple items cannot be removed after the tuple has been created.')
print_answer(True)


## Python - Access Tuple Items
print('\tPython - Access Tuple Items\n')
s = """You can access tuple items by referring to the index number,
but what is the index number of the first item?"""
print(s)
print_answer(0)


print('Use the correct syntax to print the first item in the fruits tuple.')
print_answer('print(fruits[0])')


print('Use negative indexing to print the last item in the tuple.')
print_answer('print(fruits[-1])')


print('Use a range of indexes to print the third, fourth, and fifth item ')
print('in the tuple.')
print_answer('print(fruits[2:5])')


## Python Update Tuples
print('\tPython Update Tuples\n')
print('You cannot change the items of a tuple, but there are workarounds. ')
print('Which of the following suggestion will work?')
s = 'Convert tuple into a list, change item, convert back into a tuple.'
print_answer(s)


print('Which is a correct syntax to delete a tuple?')
print_answer('del mytuple')


print('True or False. You are allowed to add a tuple to an existing tuple.')
print_answer(True)


## Python - Unpack Tuples
print('\tPython - Unpack Tuples\n') 
supply = 'Consider the following code:'
var = '(x, y, z)'
sentence_beg = 'f = ("apple", "banana", "cherry")\n{var} = f\nprint(y)'
sentence_end = '\nWhat will be the value of y?'
print(supply +  sentence_beg + sentence_end, sep='\n')
print_answer('banana')


var = '(x, *y)'
print(supply +  sentence_beg + sentence_end, sep='\n')
print_answer("['banana', 'cherry']")


var = '(x, *y, z)'
sentence_beg = 'f = ("apple", "banana", "cherry", "mango")\n{var} = f\nprint(y)'
print(supply +  sentence_beg + sentence_end, sep='\n')
print_answer("['banana', 'cherry']")


## Python Loop Tuples
print('\tPython Loop Tuples\n')
print('What is a correct syntax for looping through the items of a tuple?')
s = """for x in ('apple', 'banana', 'cherry'):
    print(x)"""
print_answer(s)


print('Insert the missing part of the while loop below to loop through ')
print('the items of a tuple.')
s = """mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1"""
print_answer(s)


print('Insert the missing part of the for loop below to loop through the ')
print('items of a tuple by using the range function to loop through the ')
print('tuple\'s index numbers.')
s = """thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])"""
print_answer(s)


## Python - Join Tuples
print('\tPython - Join Tuples\n')
print('What is a correct syntax for joining tuple1 and tuple2 into tuple3?')
print_answer('tuple3 = tuple1 + tuple2')


print('What is a legal way to turn this tuple: (1,2,3) into this ')
print('tuple:(1,2,3,1,2,3)?')
answer = """tuple1 = (1,2,3)
tuple1 = tuple1 * 2"""
print(answer)


print(supply)
s = """tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1"""
sentence_end = 'What will be the value of tuple3?'
print(s + sentence_end, sep='\n')
print_answer("(1, 2, 3, 'a', 'b', 'c')")


## Python Tuples Code Challenge
print('\tPython Tuples Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a tuple called fruits with the values "apple", "banana", "cherry"
2. Print the second item in the tuple
3. Print the number of items using len()
4. Unpack the tuple into three variables a, b, c
5. Print the variable b"""
print(s)

# Create the tuple
fruits = "apple", "banana", "cherry"
# Print the second item
print(fruits[1])
# Print the number of items
print(len(fruits))
# Unpack the tuple
(a, b, c) = fruits
# Print b
print(b)
