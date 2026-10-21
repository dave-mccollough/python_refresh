# Polymorphism

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()