### Python For Loops


from common import print_answer


print('\tPython For Loops\n')
print('What will be the result of the following code:')
s = """for x in range(3):
    print(x)"""
print(s)
print_answer('0\n1\n2\n')


print('Loop through the items in the fruits list.')
s = """fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)"""
print_answer(s)


print('In the loop, when the item value is "banana", jump directly to the ')
print('next item.')
s = """fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)"""
print_answer(s)


print('Use the range function to loop through a code set 6 times.')
s = """for x in range(6):
    print(x)"""
print_answer(s)


print('Exit the loop when x is "banana".')
s = """fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        break
    print(x)"""
print_answer(s)

## Python For Loops Code Challenge
print('Python For Loops Code Challenge')
s = """Inside the editor, complete the following steps:
1. Create a list called fruits with: 'apple', 'banana', 'cherry'
2. Write a for loop that prints each item in fruits
3. Use break to stop the loop when the item is 'banana'"""

# Create the fruits list
fruits = ["apple", "banana", "cherry"]
# Loop through fruits, break at "banana"
for x in fruits:
    print(x)
    if x == "banana":
        break
