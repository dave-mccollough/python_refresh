# Functions

- Functions reduce repetion
- Helps organize code
- Makes code easier to debug
- Function body must be indented 4 spaces

- Use `def` keyword to define a function
  - without a parameter
    - `def user_greeting():`
      - `print("Hello")`
    - to call the function
      - `user_greeting()`
  - With a parameter
    - `def user_greeting(username):`
      - `print("Hello " + username)`
    - to call the function
      - `user_greeting("Sarah")`

- Returning a value from a function
  - use the `return` keyword
  - `def add(a, b):`
    - `return a + b`