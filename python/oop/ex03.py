### Python self Parameter


from  common import print_answer


print('Python self Parameter')
print('What does the self parameter represent in a Python class?')
print_answer('A reference to the current instance of the class')


print('Where must the self parameter be placed in a method?')
print('As the first parameter')


print('Can you use a different name instead of self?')
s = "Yes, but it's strongly recommended to use 'self' as it's the"
s += "convention"
print_answer(s)


## Python self Parameter Code Challenge
print('\tPython self Parameter Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a class called Car
2. Add an __init__ method with a brand parameter, and store it as a property
3. Add a method called show that prints the brand
4. Create an object c1 of the Car class with brand "Ford"
5. Call the show method on c1
"""
print(s)

# Create the Car class
class Car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)
# Create an object
c1 = Car("Ford")
# Call the show method
c1.show()
