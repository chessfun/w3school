### Python range


from common import print_answer


print('\tPython range\n')
print('What does range(3) produce when converted to a list?')
print_answer('[0, 1, 2]')


print('Which call creates 0, 3, 6, 9?')
print_answer('range(0, 10, 3)')


print('What does list(range(3, 7)) output?')
print_answer('[3, 4, 5, 6]')


## Python Range Code Challenge
print('\tPython Range Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Use a for loop with range(6) to print numbers 0 through 5
2. Use a for loop with range() to print numbers 2 through 5"""
print(s)
# Print 0 through 5
for i in range(6):
	print(i)
# Print 2 through 5
for i in range(2, 6):
	print(i)
