### Python Arrays


from common import print_answer


print('\PtPython Arrays\n')
print('Python Lists can be used as arrays. What will be the result of the ')
print('following code:')
s = """fruits = ['apple', 'banana', 'cherry']
print(fruits[0])
"""
print(s)
print_answer('apple')


print('What is a correct Python List method used to return the number of ')
print('elements in a list?')
print_answer('len()')


print('What will be the result of the following code:')
s = """fruits = ['apple', 'banana', 'cherry']
print(len(fruits))
"""
print(s)
print_answer(3)


## Python Arrays Code Challenge
s = """Inside the editor, complete the following steps:
1. Create a list called cars with the values "Ford", "Volvo", "BMW"
2. Print the first item in the list
3. Change the second item to "Toyota"
4. Print the list
"""
print(s)
# Create a list
cars = ["Ford", "Volvo", "BMW"]
# Print the first item
print(cars[0])
# Change the second item to "Toyota"
cars[1] = "Toyota"
# Print the list
print(cars)
