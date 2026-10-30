### Python Sets


from common import print_answer


print('\tPython Sets\n')
print('Which one of these is a set?')
print_answer("myset = {'apple', 'banana', 'cherry'}")


print('Set items cannot be removed after the set has been created.')
print_answer(False)


print('Set items cannot be removed after the set has been created.')
print_answer(True)


print('Select the correct function for returning the number of items in a set:')
s = """fruits = {'apple', 'banana', 'cherry'}
print(len(fruits))"""
print_answer(s)


## Python - Access Set Items
print('\tPython - Access Set Items\n')
print('True or False. You can access set items by referring to the index.')
print_answer(False)


print('Check if "apple" is present in the fruits set.')
s = """fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")"""
print_answer(s)


print('Consider the following code:')
s = """thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)"""
print(s + 'What will be the printed result?', sep='\n')
print_answer(False)


## Python Add Set Items
print('\tPython Add Set Items\n')
print('What is a correct syntax for adding items to a set?')
print_answer('add()')


print('Use the add method to add "orange" to the fruits set.')
s = """fruits = {"apple", "banana", "cherry"}
fruits.add("orange")"""
print_answer(s)


print('Use the correct method to add multiple items (more_fruits) to ')
print('the fruits set.')
s = """fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)"""
print_answer(s)


## Remove Set Items
print('\tRemove Set Items\n')
print('What is a correct syntax for removing an item from a set?')
print_answer('remove()')


print('Use the remove method to remove "banana" from the fruits set.')
s = """fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")"""
print_answer(s)


print('Use the discard method to remove "banana" from the fruits set.')
s = """fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")"""
print_answer(s)


print('Select the correct function to remove all items from a set:')
s = """fruits = {'apple', 'banana', 'cherry'}
fruits.clear()"""
print_answer(s)


## Loop Sets
print('\tPython - Loop Sets\n')
print('What is a correct syntax for looping through the items of a set?')
s = """for x in {'apple', 'banana', 'cherry'}:
    print(x)"""
print_answer(s)


print('Insert the missing part of the for loop below to loop through ')
print('the items of a set.')
s = """myset = {'apple', 'banana', 'cherry'}
for x in myset:
    print(x)"""
print_answer(s)


print('True or False. Sets are unordered, so when you loop through ')
print('the items, the order will be totally random.')
print_answer(True)


## Python Join Sets
print('\tPython Join Sets\n')
print('What is a correct syntax for joining set1 and set2 into set3?')
print_answer('set3 = set1.union(set2)')


print('What is a correct syntax for joining multiple sets into one ')
print('new set called set5?')
print_answer('set5 = set1 | set2 | set3 | set4')


print('There are many ways to join sets in Python. Which one of the ')
print('following methods keeps ONLY the duplicates?')
print_answer('intersection()')


## Python frozenset
print('\tPython frozenset\n')
print('Which statement is true about frozenset?')
print_answer('It is an immutable set')


print('Which operation is valid on frozenset?')
print_answer('union({1,2})')


print('What is the data type of a frozenset?')
print_answer('frozenset')


## Python Sets Code Challenge
print('\tPython Sets Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a set called colors with the values "red", "green", "blue"
2. Print the set
3. Add "yellow" to the set using add()
4. Remove "green" from the set using discard()
5. Print the number of items using len()"""
print(s)
# Create the set
colors = {"red", "green", "blue"}
# Print the set
print(colors)
# Add "yellow"
colors.add("yellow")
# Remove "green"
colors.discard("green")
# Print the number of items
print(len(colors))
