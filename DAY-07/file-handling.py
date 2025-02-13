# f = open("demofile.txt")
# f = open("demofile.txt", "rt")
# print(f.read())

# f = open("demofile.txt", "r")
# print(f.read(10))

# f = open("demofile.txt", "rt")
# print(f.readline())


# f = open("demofile.txt", "r")
# print(f.readline())
# print(f.readline())


# f = open("demofile.txt", "r")
# for x in f:
#   print(x)


# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:
# f = open("demofile.txt", "r")
# print(f.read())


# f = open("demofile.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

#open and read the file after the overwriting:
# f = open("demofile.txt", "r")
# print(f.read())



f = open("demofile.txt", "r")
print(f.readline())


# import os
# os.add("demofile.txt")

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")


import sys
print(sys.version)


if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#Multiline string:
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(type(x))