### Python File Open


from common import print_answer


print('\tPython File Open\n')
print('What is a function used for opening files?')
print_answer('open()')


s = 'By default the file is opened in text mode, but you can also open the file'
s += 'in binary mode. Which one of the following syntaxes opens the file in'
s += ' binary mode?'
print(s)
print_answer("x = open('demofile.txt', 'b')")


s = "True or False. The default opening mode when opening a file with the "
s += "open() function is 'r' for 'reading'."
print(s)
print_answer(True)


## Python File Open
print('\tPython File Open\n')
s = 'After opening a file with the open() function, which method can be used'
s += ' to read the content?'
print(s)
print_answer('read()')


print('To read only one line, we can use another method, which one?')
print_answer('readline()')


s = "True or False. If you call the readline() method two times, it will return"
s += " the two first lines."
print(s)
print_answer(True)


## Python File Write
s = "What happens to the original file content if you open a file like this:"
s += "open('demofile3.txt', 'w')"
print(s)
print_answer('The original content will be overwritten')


s = "If you open a file like this:\n"
s += "with open('demofile3.txt', 'w') as f:\n"
s += "What happens if the file does not exist?"
print(s)
print_answer('A file will be created')


s = "Consider this code:\nwith open('demofile3.txt', 'w') as f:\n"
s += "What could you replace the 'w' with to instead return an error if the "
s += "file already exists?"
print(s)
print_answer("'x'")


## Python Delete File
print('\tPython Delete File\n')
s = 'To remove a file you can import the os module, but which function removes'
s += ' the file?'
print(s)
print_answer('os.remove()')


print('Which os function can be used to delete an entire folder?')
print_answer('os.rmdir()')


s = 'True or False. To remove a folder with the os module, it cannot contain '
s += ' any files'
print(s)
print_answer(True)
