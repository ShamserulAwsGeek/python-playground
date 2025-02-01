#Conditional statements in Python are used to make decisions based on the truth of an expression. 
#The value of the expression is either True or False. 
# You use the if statement to execute a block of code only if the condition is True.
# Use the else statement to execute a block of code if the condition is False. 
# Use the elif statement to specify a new condition to test, if the first condition is False.

# if example:
a = 10 
b = 20
if a > b:
    print("a is greater than b")
print("a is not greater than b")

# if else example:
a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
    
# if elif else example:
a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

#elif example:
a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")

# Nested if example:
a = 10
if a > 0:
    if a % 2 == 0:
        print("a is a positive even number")
    else:
        print("a is a positive odd number")
else:
    print("a is a negative number")
    