### Python String Formatting


from common import print_answer


print('\tPython String Formatting\n')
print('What placeholders are used when dealing with f-strings?')
print_answer('{}')


print('Use the price variable and f-string syntax to display the price with ')
print('two decimals:')
s = """price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
"""
print_answer(s)


print("Use an if statement inside the f-string placeholders to return ")
print("'perfect' if the price is 100, and 'ok' if the price is not 100:")
s = """price = 100
txt = f"It is {'perfect' if price == 100 else 'ok'}"
print(txt)
"""
print_answer(s)


print('Consider the following code:')
print("price = 1000\ntxt = f'The price is {price:,} dollars'")
print("print(txt)")
print('What will be the printed result?')
print_answer('The price is 1,000 dollars')


## Python String Formatting Code Challenge
print('\tPython String Formatting Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a variable price with the value 49
2. Create a variable txt using an f-string with price as a placeholder
3. Print txt
"""
print(s)
# Create a variable
price = 49
# Create an f-string
txt = f"The price is {price} dollars"
# Print the result
print(txt)
