### Python Lists


from common import print_answer


print('\tPython Lists\n')
print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry']\n
print(mylist[1])"""
print(s)
print_answer('banana')


print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])"""
print_answer('banana')


print('List items cannot be removed after the list has been created.')
print_answer(False)


print('Select the correct function for returning the number of items in')
print('a list:')
s = """thislist = ['apple', 'banana', 'cherry']
print(_______(thislist))"""
print(s)
print_answer('len')


## Python - Access List Items
print('\tPython - Access List Items\n')
print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])"""
print(s)
print_answer('cherry')


print('Print the second item in the fruits list.')
s = """fruits = ["apple", "banana", "cherry"]
print(________)"""
print(s)
print_answer('fruits[1]')


print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])"""
print(s)
print_answer("""['banana', 'cherry', 'orange']""")


print('Use a range of indexes to print the third, fourth, and fifth item in')
print('the list.')
s = """fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print('fruits[____])')"""
print_answer('fruits[2:5]')


## Python - Change List Items
print('\tPython - Change List Items\n')
print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])"""
print_answer('banana')


print('Change the value from "apple" to "kiwi", in the fruits list.')
s = """fruits = ['apple', 'banana', 'cherry']
________ = ________"""
print(s)
print_answer('fruits[0] = "kiwi"')


print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])"""
print(s)
print_answer('mango')


## Python - Add List Items
print('\tPython - Add List Items\n')
print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])"""
print(s)
print_answer("'apple'")


print('Use the append method to add "orange" to the fruits list.')
print('fruits = ["apple", "banana", "cherry"]')
print_answer('fruits.append("orange")')


print('Use the insert method to add "lemon" as the second item in the')
print('fruits list.')
print('fruits = ["apple", "banana", "cherry"]')
print_answer('fruits.insert(1, "lemon")')


print('Select the missing parts to add the elements of tropical to fruits:')
s = """fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']"""
print(s)
print_answer('fruits.extend(tropical)')


## Python - Remove List Items
print('\tPython - Remove List Items\n')
print('What is a List method for removing list items?')
print_answer('pop()')


print('Use the remove method to remove "banana" from the fruits list.')
print('fruits = ["apple", "banana", "cherry"]')
print_answer('fruits.remove("banana")')


print('What will be the result of the following syntax:')
s = """mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)"""
print(s)
print_answer("['apple', 'cherry']")


print('Select the correct function to remove all items from a list:')
print("fruits = ['apple', 'banana', 'cherry']")
print_answer('fruits.clear()')


## Python - Loop Lists
print('\tPython - Loop Lists\n')
print('What is a correct syntax for looping through the items of a list?')
print_answer("for x in ['apple', 'banana', 'cherry']:\n    print(x)")


print('Insert the missing part of the while loop below to loop through ')
print('the items of a list.')
s = """mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1"""
print_answer(s)


print('What is a correct syntax for looping through the items of a list?')
print_answer("""[print(x) for x in ['apple', 'banana', 'cherry']]""")


## Python - List Comprehension
print('\tPython - List Comprehension\n')
s = """fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']"""
print('Consider the following code:')
print(s)
print('What will be the value of newlist?')
print_answer("['banana']")


print('Fill in the missing parts to complete the list comprehension:')
print('fruits = ["apple", "banana", "cherry"]')
print_answer('newlist = [x for x in fruits]')


print('Consider the following code:')
s = """fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]"""
print(s)
print('What will be the value of newlist?')
print_answer("['apple', 'apple', 'apple']")


## Python - Sort Lists
print('\tPython - Sort Lists\n')
print('What is a correct syntax for sorting a list?')
print_answer('mylist.sort()')


print('What is a correct syntax for reversing the current order of a list?')
print_answer('mylist.reverse()')

print('What is a correct syntax for sorting a list descending?')
print_answer('mylist.sort(reverse = True)')


## Python - Copy Lists
print('(\tPython - Copy Lists\n')
print('What is a correct syntax for making a copy of a list?')
print_answer('list2 = list1.copy()')
print_answer('list2 = list(list1)')
print_answer('list2 = list1[:]')


## Python - Join Lists
print('\tPython - Join Lists\n')
print('What is a correct syntax for joining list1 and list2 into list3?')
print_answer('list3 = list1 + list2')
print_answer('list1.extend(list2)')


prit('Consider the following code:')
s = """list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)"""
print(s + '\nWhat will be the value of list1?')
print_answer('['a', 'b', 'c', 1, 2, 3]')


## Python Lists Code Challenge
s = """Inside the editor, complete the following steps:
Create a list called colors with the values \"red\", \"green\", \"blue\"
Print the first item in the list
Change the second item to \"yellow\"
Add \"purple\" to the end of the list using append()
Remove \"red\" from the list using remove()
Print the list"""
# Create a list
colors = ["red", "green", "blue"]
# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[1] = "yellow"
# Add "purple" to the end
colors.append("purple")
# Remove "red"
colors.remove("red")
# Print the list
print(colors)
