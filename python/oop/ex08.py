### Python Polymorphism


from common import print_answer


print('\tPython Polymorphism\n')
s = "True or False. One object cannot have a method with the same name as "
s += "another object's method."
print(s)
print_answer(False)


s = "True or False. Methods with the same name, but for different objects, "
s += "can have different content, but the return value has to be of same "
s += "data type."
print(s)
print_answer(False)


print('Which statement is true?')
s = "Polymorphism refers to methods/functions/operators with the same name"
s += " that can be executed on many objects or classes."
print_answer(s)


## Python Polymorphism Code Challenge
s = """Inside the editor, complete the following steps:
1. Create a class Cat with a method sound that prints "Meow"
2. Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
3. Create objects c1 = Cat() and f1 = Fox()
4. Call sound() on both objects
"""
print(s)

# Create the Cat class
class Cat:
    def sound(self):
        print("Meow")

# Create the Fox class
class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")

# Create objects and loop
c1 = Cat()
f1 = Fox()
c1.sound()
f1.sound()
