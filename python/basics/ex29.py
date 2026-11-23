### Python RegEx


from common import print_answer


print('\tPython RegEx\n')
print('Consider the following code:')
s = """import re
txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)
"""
print(s)
print('What will be the printed result?')
print_answer("['a', 'a']")


print('Consider the following code:')
s = """import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())
"""
print(s)
print('What will be the printed result?')
print_answer(3)


print('When using the re module to find a match, a match will return a Match ')
print('object, but what is the return value when there is no match?')
print_answer(None)


## Python RegEx Code Challenge
print('\tPython RegEx Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Import the re module
2. Create a variable txt with the value "The rain in Spain"
3. Search for "Spain" in txt and store the result in x
4. Print the position (span) of the match
"""
print(s)
# Import re
import re
# Create a string
txt = "The rain in Spain"
# Search for "Spain"
x = re.search("Spain", txt)
# Print the span
print(x.span())
