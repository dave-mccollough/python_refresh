# Loops

# For Loops

mountains = ["Longs Peak", "Mount Blue Sky", "Pikes Peak"]

for mountain in mountains:
    print(mountain)


# Iterating through each character in a string
name = "Sarah"

for char in name:
    print(char)


# While Loops

count = 0

while count <= 5:
    print(count)
    count += 1


# User input with a while loop

secret = ''

while secret != "Python123":
    secret = input("What is the secret? ")

print("Access Granted!")