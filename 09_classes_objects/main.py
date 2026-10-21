# Classes

class Car:
    # variables for class
    wheels = 4
    color = "Blue"
    make = "Jeep"
    model = "Wrangler"

    # function to describe variables
    # self is the current object
    def show_details(self):
        print("Car make: ", self.make)
        print("Car model: ", self.model)
        print("Car color: ", self.color)
        print("Number of wheels: ", self.wheels)

# Create an object
car1 = Car()

# Call the function
car1.show_details()


# Create an object
car2 = Car()

# Call the function
car2.show_details()