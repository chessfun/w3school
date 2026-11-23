### Python While Loops


from common import print_answer


print('\tPython While Loops\n')
print('Which statement is a correct syntax to break out of a loop?')
print_answer('break')


print('Print i as long as i is less than 6.')
s = """i = 1
while i < 6:
    print(i)
    i += 1
"""
print_answer(s)


print('Stop the loop if i is 3.')
s = """i = 1
while i < 6:
    if i == 3:
        break
    i += 1
"""
print_answer(s)


print('In the loop, when i is 3, jump directly to the next iteration.')
s = """i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
"""
print_answer(s)


print('Print a message once the condition is false.')
s = """i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')
"""
print_answer(s)


## Python While Loops Code Challenge
s = """Inside the editor, complete the following steps:
1. Create a variable i with the value 0
2. Write a while loop that runs as long as i is less than 6
3. Inside the loop: increment i by 1
4. If i equals 3, use continue to skip that iteration
5. Print i"""
print(s)
# Create the i variable
i = 0
# While loop: print 1-5, skip 3 with continue
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
