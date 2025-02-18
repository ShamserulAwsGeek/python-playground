# for i in range(4):
#     print("Sham Loves Maheen")

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number == 3:
#         break
#     print(number)

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number == 3:
#         continue
#     print(number)

#while loop:
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# log_file = [
#    "INFO: Operation successful",
#    "ERROR: File not found",
#    "DEBUG: Connection established",
#    "ERROR: Database connection failed",
# ]

# for line in log_file:
#    if "ERROR" in line:
#        print(line)

servers=("server1" "server2" "server3")
for server in "${servers[@]}": 
    #configure_monitoring_agent "$server"
    print(server)
