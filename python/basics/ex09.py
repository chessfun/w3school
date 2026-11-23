### Python Casting


from common import print_answer


def help_foo(question, answer):
    print('What will be the result of the following code: {question}', question)
    print_answer(answer)

    
print('Python Casting')
help_foo('print(int(35.88))', 35)
help_foo('print(float(35))', 35.0)
help_foo('print(str(35.82))', '35.82')


## Python Casting Code Challenge

print('Python Casting Code Challenge')
tmp_str = """Inside the editor, complete the following steps:
Create a variable x with the integer value 1
Convert x to a float and store it in a
Convert x to a string and store it in b
Print a and b
"""
print(tmp_str)

# Create an integer
x = 1
# Convert to float
a = float(x)
# Convert to string
b = str(x)
# Print values

print(a, b)
