#Here, the show method in the Child class overrides the one in the Parent class.
class Parent:
def show(self):
print("This is the parent class.")

class Child(Parent):
def show(self):
print("This is the child class.")

# Usage
obj = Child()
obj.show() # Output: This is the child class

#Using super() to Call Parent Method:
class Parent:
def show(self):
print("This is the parent class.")

class Child(Parent):
def show(self):
super().show()
print("This is the child class.")

# Usage
obj = Child()
obj.show()
# Output:
# This is the parent class
# This is the child class
