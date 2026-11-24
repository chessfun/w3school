### Python Inner Classes


from common import print_answer


print('\tPython Inner Classes\n')
print('What is an inner class in Python?')
pritn_answer('A class defined inside another class')


s = 'How do you create an object of an inner class '
s += 'from outside the outer class?'
print(s)
s = 'First create an outer class object, then use it to '
s += 'create the inner class object'
print_answer(s)


print('What will be the result of the following code:')
s = """
class Outer:
    class Inner:
        def display(self):
            print("Hello")

outer = Outer()
inner = outer.Inner()
inner.display()
"""
print(s)
print_answer(s)
