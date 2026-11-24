### Python Encapsulation


from common import print_answer


print('\tPython Encapsulation\n')
print('How do you make a property private in Python?')
print_answer('Use a double underscore prefix: __property;')


print('What will be the result of the following code:')
s = """
class Person:
    def __init__(self, age):
        self.__age = age

p1 = Person(25)
print(p1.__age)
"""
print(s)
print_answer('Error')


print('What is the purpose of encapsulation?')
print_answer('To protect data and control how it can be accessed')


## Python Encapsulation Code Challenge
print('\tPython Encapsulation Code Challenge\n')
s = """
1. Inside the editor, complete the following steps:
2. Create a class ScoreBoard
3. Add an __init__ with a score parameter and store it as a private attribute
4. Add a method called get_score that returns the private score
5. Create an object s1 with a score of 0
6. Print the score of s1
"""
print(s)

# Create the ScoreBoard class
class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


# Create an object
s1 = ScoreBoard(0)
# Print the score
print(s1.get_score())
