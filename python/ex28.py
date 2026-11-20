### Python JSON


from common import print_answer


print('\tPython JSON\n')
print('When you parse code with the json.loads() method, the result is ')
print('returned as a specific Python data type, which one?')
print_answer('dictionary')


print('Which method from the json library can be used to convert a Python ')
print('object into a JSON string?')
print_answer('json.dumps()')


print('The json.dumps() method has a keyword parameter used to sort the ')
print('result, what is it called?')
print_answer('sort_keys')


## Python JSON Code Challenge
print('\tPython JSON Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Import the json module
2. Create a variable x with this JSON string: '{"name": "Emil", "age": 30}'
3. Convert the JSON string into a Python dictionary and store it in y
4. Print the age from y
"""
print(s)
# Import json
import json
# Create a JSON string
x = '{"name": "Emil", "age": 30}'
# Parse the JSON string
y = json.loads(x)
# Print the age
print(y["age"])
