# Conditional Statements

## If block
age = 25

if age >= 21:
    print('You can legally drink alcohol.')


## if - else block

score = 85

if score >= 60:
    print("You passed")
else:
    print("You did not pass")

## if - elif - else block

grade = 82

if grade >= 90:
    print("Your grade is A")
elif grade >= 80 and grade < 90:
    print("Your grade is B")
elif grade >= 70 and grade < 80:
    print("Your grade is a C")
elif grade >= 60 and grade < 70:
    print("Your grade is a D")
else:
    print("You did not pass")

# Match Case

return_status = 900

match return_status:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 404:
        print("Not Found")
    case _: # This handles any cases that don't match
        print("Status Unknown")
