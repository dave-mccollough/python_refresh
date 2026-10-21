# Constructors

class Car:
    # variables for class
    wheels = 4
    color = ""
    make = ""
    model = ""

    def __init__(self, car_color, car_make, car_model):
        self.color = car_color
        self.make = car_make
        self.model = car_model


        
    def show_details(self):
        print("Car make: ", self.make)
        print("Car model: ", self.model)
        print("Car color: ", self.color)
        print("Number of wheels: ", self.wheels)


car1 = Car("Earl Gray", "Jeep", "Wrangler")
car1.show_details()

car2 = Car("White", "Nissan", "Envy")
car2.show_details()