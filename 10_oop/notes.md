# Object Oriented Programming (OOP)

- Provides a clear structure to programs
- Makes code easier to maintain, resuse and debug
- Helps keep code DRY (do not repeat yourself)

## OOP Pillars

- Encapsulation
  - Bundles data and methods in an object. Interal details are abstracted
- Inheritance
  - New objects inherit properties from existing ones
  - Build once, extend many times
- Polymorphism
  - Objects can be treated as instances of a parent class
  - Enables flexible and reusable behavior
- Abstraction
  - Hides unecessary complexity
  - Only exposes what is necessary for user or developer

## Inheritance

- Inheritance allows a child class (subclass) to automatically inherit/acquire the properties and behaviors of a parent class (supercalss)
- Think of it as a template you can extend


## Encapsulation

- Keeps data and methods together
  - Data and methods live together in a class
- Don't allow variables to be accessed directly in other classes
- Getter function
  - Function to get private variable value
- Use leading `__` on variable name to make it private
  - `__salary = 1000`