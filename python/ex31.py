### Python Try Except


from common import print_answer


print('\tPython Try Except\n')
print('In a try...except block, there is a certain block that if specified, ')
print('will be executed regardless if the try block raises an error or not. ')
print('What is the name of this block?')
print_answer('finally')


print('Fill in the missing code in this try...except example:')
s = """try:
    print(x)
except:
    print("An exception occurred")
"""
print_answer(s)


print('Fill in the missing code in this try...except example, the last code ')
print('block should be executed if there are no errors:')
s = """try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
"""
print_answer(s)


## Python Try...Except Code Challenge
print('\tPython Try...Except Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Write a try block that tries to print a variable x (which is not defined)
2. Write an except block that prints "An error occurred"
3. Write a finally block that prints "Execution complete"
"""
print(s)
# Try to print x
try:
	print(x)
except:
	print("An error occurred")
finally:
	print("Execution complete")
