# Inheritance

class Vehicle:
    wheels = 4
    def move(self):
        print("Moving forward...")

class Rentable:
    def rent(Self):
        print("This vehicle is for rent")

class Car(Vehicle, Rentable):
    def sound(self):
        print("Honk!")

class Bike(Car):
    def bell(Self):
        print("Ring!")




bike1 = Bike()
bike1.move()
bike1.bell()
bike1.sound()
car1 = Car()
car1.rent()