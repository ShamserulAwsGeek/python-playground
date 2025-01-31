# Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
def sham(name):
    print("Hello "  + name)
message = sham("Maheen")
print(message)

# Modules are Python files that consist of Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.

#my_module.py
def square(x):
    return x ** 2

pi = 3.14159265

# Importing Modules
import my_module
print(my_module.square(3))
print(my_module.pi)

#import the entire module:
import math

#use functions/variables from the module:
math.sqrt(16)

#import specifiv functions/variables from the module:
from math import sqrt
print(sqrt(16))

