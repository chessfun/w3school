### Python Dictionaries


from common import print_answer


print('\tPython Dictionaries\n')
print('Which one of these is a dictionary?')
print_answer("x = {'type' : 'fruit', 'name' : 'banana'}")


print('Dictionary items cannot be removed after the dictionary has ')
print('been created.')
print_answer(False)


print('A dictionary cannot have two keys with the same name.')
print_answer(True)


print('Select the correct function to print the number of key/value ')
print('the dictionary:')
s = """x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))"""
print_answer(s)


## Access Dictionary Items
print('\tAccess Dictionary Items\n')
print('You can access item values by referring to the key name.')
print_answer(True)


print('Use the get method to print the value of the "model" key of ')
print('the car dictionary.')
s = """car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))"""
print_answer(s)


print('Consider the following code:')
s = """x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])"""
print(s + 'What will be the printed result?', sep='\n')
print_answer('fruit')


## Python Change Dictionaries
print('\tPython Change Dictionaries\n')
print('Consider the following code:')
s = """x = {'type' : 'fruit', 'name' : 'banana'}
What is a correct syntax for changing the type from fruit to berry?"""
print(s)
print_answer("x['type'] = 'berry'")


print('Change the "year" value from 1964 to 2020.')
s = """car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020"""
print_answer(s)


print('Consider the following code:')
print("x = {'type' : 'fruit', 'name' : 'banana'}")
print('What is a correct syntax for changing the name from banana to apple?')
print_answer("x.update({'name': 'apple'})")


## Add Dictionary Items
print('\tAdd Dictionary Items\n')
print('Which one of these dictionary methods can be used to add items ')
print('to a dictionary?')
print_answer('update()')


print('Add the key/value pair "color" : "red" to the car dictionary.')
s = """car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
"""
print_answer(s)


print('Insert themissing part to add an item to the dictionary.')
s = """x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' : 'green'})"""
print_answer(s)


## Remove Dictionary Items
print('\tRemove Dictionary Items\n')
print('What is a dictionary method for removing an item from a dictionary?')
print_answer('pop()')


print('Use the pop method to remove "model" from the car dictionary.')
s = """car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")"""
print_answer(s)


print('Use the clear method to empty the car dictionary.')
s = """car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()"""
print_answer(s)


print('Insert a correct syntax for removing the \'color\' item of the dictionary:')
s = """myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar['color']"""
print_answer(s)


## Python Loop Dictionaries
print('\tPython Loop Dictionaries\n')
var = 'the values'
ask = 'What is a correct syntax for looping through the {var} of '
dic = 'this dictionary:\n\tx = {"type" : "fruit", "name" : "apple"}'
print(ask)
print(dic)
print_answer('for y in x.values():\n    print(y)')


print('Is it possible to loop through the keys of a dictionary?')
print_answer(True)


var = 'the keys AND values'
print(ask)
print(dic)
print_answer('for y, z in x.items():\t    print(y, z)')


var = 'the keys'
print(ask)
print(dic)
print_answer('for y in x.keys():\t    print(y)')


## Python Copy Dictionaries
print('\tPython Copy Dictionaries\n')
print('What is a correct syntax for making a copy of this dictionary:')
print_answer('y = x.copy()')


print('One of these codes is NOT a correct way of making a copy of a dictionary ')
print('named x, which one:')
print_answer('y = x.duplicate()')


print('Copied dictionaries will not be able to change its item values.')
print_answer(False)


## Nested Dictionaries
print('\tNested Dictionaries\n')
print('Consider this syntax:')
s = """a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}"""
print(s)
print('what will be a correct syntax for printing the name \'May\'?')
print_answer('print(customers[\'c2\'][\'name\'])')


print('Insert the missing part to loop through the keys and values of all ')
print('nested dictionaries:')

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}

for x, obj in customers.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
print_answer('items()')


print('A dictionary can only have one level of nested dictionaries.')
print_answer(False)


## Python Dictionaries Code Challenge
print('\tPython Dictionaries Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
2. Print the value of the "model" key
3. Add a new key "color" with the value "red"
4. Remove the "brand" key using pop()
5. Print the dictionary"""
print(s)
# Create the dictionary
car = {
	"brand": "Frod",
	"model": "Mustang",
	"year": 2024
}
# Print the model
print(car['model'])
# Add a color key
car.update({"color": "red"})
# Remove the brand key
car.pop("brand")
# Print the dictionary
print(car)
