

# Read a file
#Mode is r
with open(".../11_file_handling/data.txt", "r") as file_object:
    file_content = file_object.read()
    print(file_content)

# Write file
# Mode is w
with open(".../11_file_handling/data.txt", "w") as file_object:
    file_object.write("So many cool mountains! \n")
    file_object.write("Here in CO! \n")


# Appending to a file
# mode is a
with open(".../11_file_handling/data.txt", "a") as file_object:
    file_object.write("Front Range Fourteeners: \n")
    file_object.write("- Pikes Peak \n")
    file_object.write("- Mount Blue Sky \n")
    file_object.write("- Mount Bierstadt \n")
    file_object.write("- Longs Peak \n")
    file_object.write("- Grays Peak \n")
    file_object.write("- Torreys Peak\n")

    

