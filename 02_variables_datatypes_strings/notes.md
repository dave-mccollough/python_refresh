# Variables, Data Types and Strings

## Variables

- Variables are named containers to store data
  - `my_age = 30`
- Can contain numbers, text or boolean values
- Value can change - dynamically typed
- Use snake_case for variable names
- Variable names can't start with a number or a Python keyword
  - `if, for, while`
- Use ALL_CAPS for variable names of static values/constants
  - `MAX_CONNECTIONS = 100`

## Data Types

- Data types tell Python's interpreter how to handle data and which operations are valid
- Commonly used data types
  - `int`
    - Integer
      - `number = 12`
  - `float`
    - Decimal
      - `price = 12.99`
  - `str`
    - String
      - `name = "Dave"`
  - `list`
    - Ordered and mutable
      - `fruits = ["Apple", "Banana", "Orange"]`
  - `dict`
    - Dictionary
    - Stores key value pairs
      - `user_details = {"name": "Dave", "age" 30}`
  - `bool`
    - Stores boolean values - True/False
      - `is_active = True`
  - `tuple`
    - Ordered and immutable
      - `coords = (12.4, -0.13)`
  - `set`
    - Unique elements
    - Removes duplicates
      - `fruits = {"Apple", "Grape", Apple}`

## Type

- use `type()` to get data type of a variable
  - `print(type(<variable_name>))`

## Strings

- Sequence of characters
- Strings are immutable. Any modification creates a new string object in memory

## String functions

- Case conversion
  - `.lower()`
    - Convert all characters to lowercase
  - `.upper()`
    - Convert all characters to uppercase
- Starts/Ends with
  - `.startswith()` or `.endswith()`
    - Returns `True` or `False` depending on the string boundaries
- Search and Find
  - `.find()`
    - Returns the index of a substring
  - `.count()`
    - Counts how many times it appears
- Replace and strip
  - `.replace()`
    - Swaps substrings
  - `.strip()`
    - Removes leading and trailing whitespace

## String Slicing

- Use `[start:stop]` syntax to extract a portion of a string
- Count starts at `0`
- Slice from start
  - `variable_name[:stop_index]`
- Slice from end
  - `variable_name[:start_index]`
- Slice a specific range
  - `variable_name[start_index:stop_index]`
