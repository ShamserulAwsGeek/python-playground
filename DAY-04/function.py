# Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
def sham(name):
    print("Hello "  + name)
message = sham("Maheen")
print(message)

# Modules are Python files that consist of Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.

#my_module.py
# def square(x):
#     return x ** 2

# pi = 3.14159265

# Importing Modules
# import my_module # type: ignore
# print(my_module.square(3))
# print(my_module.pi)

#import the entire module:
#import math

#use functions/variables from the module:
#math.sqrt(16)

#import specifiv functions/variables from the module:
# from math import sqrt
# print(sqrt(16))


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def sham(name):
    print("Sham " + name)
sham("Maheen")

x = 10
y = 20

def add():
    add = x + y
    print(add)
def sub():
    sub = x - y
    print(sub)
def mul():
    mul = x * y
    print(mul)
def div():
    div = x / y
    print(div)

add()
sub()
mul()
div()

x = 10
y = 20

def calc():
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
add()
sub()
mul()
div()

def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)


def namelist(names):
     return ", ".join(names)
message = namelist(["Alice", "Bob", "Charlie"])
print(message)

def my_function(name):
  print(name +  " Refsnes " )

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Maheen")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass


def my_function(x,/):
  print(x)

my_function(3)


#Recursion:

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)