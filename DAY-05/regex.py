#RegEx: 
# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# 2. Write a Python program that matches a string that has an 'a' followed by zero or more b's.
# 3. Write a Python program that matches a string that has an 'a' followed by one or more b's.
# 4. Write a Python program that matches a string that has an 'a' followed by zero or one 'b'.
# 5. Write a Python program that matches a string that has an 'a' followed by three 'b'.
# 6. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
# 8. Write a Python program to find sequences of one upper case letter followed by lower case letters.
# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# 10. Write a Python program that matches a word at the beginning of a string.
# 11. Write a Python program that matches a word at the end of string, with optional punctuation.
# 12. Write a Python program that matches a word containing 'z'.
# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# 15. Write a Python program where a string will start with a specific number.


import re
def check_string(string):
    pattern = re.compile(r'[^a-zA-Z0-9.]')
    if pattern.search(string):
        print("The string contains special characters.")
    else:
        print("The string does not contain special characters.")

def match_string(string):
    pattern = re.compile(r'ab*')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string1(string):
    pattern = re.compile(r'ab+')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string2(string):
    pattern = re.compile(r'ab?')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string3(string):
    pattern = re.compile(r'ab{3}')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string4(string):
    pattern = re.compile(r'ab{2,3}')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string5(string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string6(string):
    pattern = re.compile(r'[A-Z][a-z]+')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string7(string):
    pattern = re.compile(r'a.*b$')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string8(string):
    pattern = re.compile(r'^[a-zA-Z]+')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string9(string):
    pattern = re.compile(r'[a-zA-Z]+[.,]?')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string10(string):
    pattern = re.compile(r'\b\w*z\w*\b')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string11(string):
    pattern = re.compile(r'\b\w*z\w*\b')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")


def match_string12(string):
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")

def match_string13(string):
    pattern = re.compile(r'^[0-9]+')
    if pattern.match(string):
        print("Matched!")
    else:
        print("Not matched!")


check_string("Hello@123")
match_string("ab")
match_string1("ab")
match_string2("ab")
match_string3("abbbb")
match_string4("abbb")
match_string5("hello_world")
match_string6("Hello")
match_string7("a123b")
match_string8("Hello")
match_string9("Hello.")
match_string10("Hello")
match_string11("Hello")
match_string12("Hello_123")
match_string13("123Hello")

  