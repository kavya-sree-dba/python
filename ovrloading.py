#Example Using Default Arguments:
class Greeting:
   def greet(self, name, age=None):
       if age:
           print(f"Hello, {name}! You are {age} years old.")
       else:
           print(f"Hello, {name}!")
# Usage
obj = Greeting()
obj.greet("Alice") # Output: Hello, Alice!
obj.greet("Bob", 25) # Output: Hello, Bob! You are 25 years old

#Example Using *args:
class Calculator:
   def add(self, *args):
       print(f"Sum: {sum(args)}")
# Usage
calc = Calculator()
calc.add(5, 10) # Output: Sum: 15
calc.add(1, 2, 3, 4, 5) # Output: Sum: 15
