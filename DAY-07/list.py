# List in Python:
# - list is a collection of items.
# - list is a mutable data type.
# - list is ordered

# Creating a list:
# - list can be created by using [] or list() constructor.
# - list can contain any type of data type.
# - list can contain duplicate values.
# - list can contain nested list.
# - list can contain different data types.
# - list can contain mutable data types.

# Accessing elements in list:
# - list can be accessed by using index.
# - index starts from 0.
# - index can be negative.
# - index can be slice
    
# Updating elements in list:
# Deleting elements in list:
# List methods:
# List operations:
# List comprehension:
# List functions:
#   - len()
#  - min()
# - max()
# - sum()
# - sorted()
# - reversed()
# - any()
# - all()
# - enumerate()
# - zip()
# - filter()
# - map()
# - reduce()
# - lambda()
# - list()
# - tuple()
# - set()
# - dict()
# - frozenset()
# - range()
# - xrange()
# - type()
# - id()
# - isinstance()
# - issubclass()
# - getattr()
# - setattr()
# - delattr()
# - hasattr()
# - vars()
# - locals()
# - globals()
# - dir()
# - help()
# - input()


servers = list(("web-server-01", "db-server-01", "app-server-01"))
print(servers[0])
print(type(servers))

mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-3])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1