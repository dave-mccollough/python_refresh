# Functions

# Without paramaters
def add_numbers():
    a = 10
    b = 20
    print(a + b)

add_numbers()


# With parameters
def print_username(username):
    print("Welcome " + username)

print_username("John")

# Returning values from a function

def add_values(value_1, value_2):
    return value_1 + value_2

result = add_values(10, 10)
print(result)
# or....
print(add_values(20, 40))