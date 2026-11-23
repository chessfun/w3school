### Python Class Properties


from  common import print_answer


print('\tPython Class Properties\n')
print('How do you access a property of an object?')
print_answer('Using dot notation: object.property')


print('What will be the result of the following code: (see comment below)')
# class Person:
#   lastname = "Jackson"

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Emil")
# p2 = Person("Tobias")
# Person.lastname = "Hansen"
# print(p1.lastname)
print_answer('Hansen')


print('Which keyword is used to delete a property from an object?')
print_answer('del')


## Python Class Properties Code Challenge
print('\tPython Class Properties Code Challenge\n')
s = """Inside the editor, complete the following steps:
1. Create a class Student with an __init__ that takes name and grade, and stores them as properties
2. Create an object s1 with name "Anna" and grade "A"
3. Print the grade of s1
4. Change the grade of s1 to "B"
5. Print the updated grade
"""
print(s)
# Create the Student class
class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

# Create an object
s1 = Student("Anna", "A")
# Print the grade
print(s1.grade)
# Change the grade
s1.grade = "B"
# Print the updated grade
print(s1.grade)
