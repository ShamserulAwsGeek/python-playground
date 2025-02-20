my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict.get('name'))  # Output: John
print(my_dict.get('age'))  # Output: 25
#print(my_dict.get('city'))  # Output: New York

#del my_dict['city']  # Removing a key-value pair

if 'city' in my_dict:
    print('City is present in the dictionary')

for key, value in my_dict.items():
    print(key, value)