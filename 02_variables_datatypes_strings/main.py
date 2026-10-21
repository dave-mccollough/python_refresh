# Variables, Data Types and Strings

# Creating variables
user_name = "Bob"
user_age = 25
is_active = True
PI = 3.14159

# Using variables
print(user_name)
print(user_age)

# Updating variable value
user_age = 26
print(user_age)


# Using type()

name = "Susan"
number = "23"
price = 12.99
is_available = True

print(type(name)) #<class 'str'>
print(type(number)) #<class 'str'>
print(type(price)) #<class 'float'>
print(type(is_available)) #<class 'bool'>

# Strings

user_message = "Hello"
print(user_message)

user_message = user_message + " Python"
print(user_message)

# Different ways to create strings

# Single quotes
# Most common and concise way to create strings
my_string = 'Hello World!'

# Double Quotes
# Use when strings contain an apostrophe or single quote
double_string = "Python's fun!"

# Triple quotes
# Use for multi-line strings
message = """Line one
and line two
and line three
"""
print(message)

# String Methods
# Case conversion
new_message = " Hello User "
print(new_message.upper()) # HELLO USER
print(new_message.lower()) # hello user

# Starts/Ends with
print(new_message.startswith("H")) # True
print(new_message.endswith('U')) # False

# Find and count
print(new_message.find("o")) # 4
print(new_message.count("e")) # 2

# Replace
print(new_message.replace("ll", "dd")) # Heddo User

# Strip
print(new_message.strip())

# String slicing
programming_language = "Python"
print(programming_language[:3]) # Pyt
print(programming_language[2:]) # thon
print(programming_language[2:4]) # th


