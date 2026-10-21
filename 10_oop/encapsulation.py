# Encapsulation

class Employee:
    name = "John"
    # Make salary private
    __salary = 1000

    # Define getter function
    def show_salary(self):
        return self.__salary

class Run:
    e = Employee()
    print(e.name)
    print(e.show_salary())