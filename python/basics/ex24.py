### Python Iterators


from common import print_answer


print('\tPython Iterators\n')
print('There are two methods that you have to implement when you create an ')
print('iterator, which two?')
print_answer('__iter__() and __next__()')


print('Which statement can be used to stop the iteration?')
print_answer('StopIteration')


print('True or False. Lists, tuples, dictionaries, and sets are all ')
print('iterable objects.')
print_answer(True)


## Python Iterators Code Challenge
print('\tPython Iterators Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a tuple called mytuple with the values "apple", "banana", "cherry"
2. Create a variable myit and use iter() on the tuple
3. Print the first item using next()
"""
print(s)
# Create a tuple
mytuple = ("apple", "banana", "cherry")
# Create an iterator
myit = iter(mytuple)
# Print the first item
print(next(myit))
