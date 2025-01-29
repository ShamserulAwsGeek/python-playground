# Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
def sham(name):
    print("Hello "  + name)
message = sham("Maheen")
print(message)

# Modules are Python files that consist of Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.
# sham_module.py
def square(x):
    return x * x
pi = 3.1416

# import sham_module
import sham_module
result = sham_module.square(3)
print(result)
print(sham_module.pi)
