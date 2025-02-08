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


# import sys
# type = sys.argv[1]

# if type == "t2.micro":
#     print("This is a micro instance")
# else:
#     print("This is a small instance")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#Nested if example:
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#Loop A loop is a sequence of instructions that is continually repeated until a certain condition is reached.

#Python has two primitive loop commands:    while loops    for loops

#The while Loop With the while loop we can execute a set of statements as long as a condition is true.
 
#Example while loop:
i = 1
while i < 6:
    print(i)
    i += 1

#The break Statement With the break statement we can stop the loop even if the while condition is true.

#Example break statement:
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

#The continue Statement With the continue statement we can stop the current iteration, and continue with the next.

#Example continue statement:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#The else Statement With the else statement we can run a block of code once when the condition no longer is true.

#Example else statement:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

