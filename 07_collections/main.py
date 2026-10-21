
# Lists

my_list = []

# use .append to add items to list
my_list.append("Apple")
my_list.append(12)
my_list.append(True)

print(my_list) # ["Apple", 12, True]

# Print element based on index
print(my_list[0]) # Apple

# Update item in a list
my_list[0] = "Banana"
print(my_list[0]) # Banana

# Delete item in a list
del my_list[2]
print(my_list) # ["Banana", 12]

# Sets

mummy_peaks = {"Chapin", "Chiquita", "Ypsilon"}
print(mummy_peaks) # {"Ypsilon", "Chapin", "Chiquita"}
# Add item to set
mummy_peaks.add("Fairchild")
print(mummy_peaks) # {"Ypsilon", "Chapin", "Fairchild", "Chiquita"}
# Add duplicate item to set
mummy_peaks.add("Chapin")
print(mummy_peaks) # {"Chapin", "Chiquita", "Ypsilon", "Fairchild"}
# Remove item from set
mummy_peaks.remove("Fairchild")
print(mummy_peaks) # {"Chapin", "Chiquita", "Ypsilon"}

# Iterate over set using for loop

for peak in mummy_peaks:
    print(peak)

# Tuples

front_range = ("Longs Peak", "Pikes Peak", "Mount Blue Sky", "Mount Bierstadt")
# Get index
print(front_range[1]) # Pikes Peak

# Get slice
print(front_range[1:3]) # ('Pikes Peak', 'Mount Blue Sky')

# For loop
for peak in front_range:
    print(peak)


# Dictionaries

user_data = {
    "username": "jsmith", 
    "account_type": "Premium", 
    "is_active": True
}

# Get specific values
print(user_data["username"]) # jsmith
print(user_data["is_active"]) # True

# Update value in dictionary
user_data["account_type"] = "Pro"
print(user_data) # {'username': 'jsmith', 'account_type': 'Pro', 'is_active': True}

# Add a new value to dictionary
user_data["email"] = "jsmith@xyzcorp.com"
print(user_data) # {'username': 'jsmith', 'account_type': 'Pro', 'is_active': True, 'email': 'jsmith@xyzcorp.com'}

# Delete items in a dictionary
del user_data["email"]
print(user_data) # {'username': 'jsmith', 'account_type': 'Pro', 'is_active': True}

# Check if key exists
if "email" in user_data:
    print("Key exists")
else:
    print("Key does not exist")

# Key does not exist