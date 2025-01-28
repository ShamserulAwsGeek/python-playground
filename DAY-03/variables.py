# assigning value to variable
my_variable = 10
print(my_variable)

#Local scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# def myfunc():
#   x = 300
#   print(x)
# myfunc()
# print(x) # NameError: name 'x' is not defined  

#Global scope: A variable created in the main body of the Python code is a global variable and belongs to the global scope.
y = 300
def myfunc():
  print(y)
myfunc()
print(y)  

# Define configuration details for a webserver
server_name = "localhost"
port = 8080
is_https_enabled = True
max_connections = 1000

# Print the configuration details
print("Server Name:", server_name)
print("Port:", port)
print("Is HTTPS Enabled:", is_https_enabled)
print("Max Connections:", max_connections)

