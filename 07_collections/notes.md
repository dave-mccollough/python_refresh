# Python Collections

## list

- Mutable
  - Can be changed after creation
- Ordered
  - Items maintain their position in the list
- Heterogeneous
  - Can hold mixed data types
- Dynamic
  - Can grow or shrink in size
- Allows you to add duplicate items
- Creating a list
  - Empty List
    - `my_list = []`
  - List with mixed data types
    - `my_list = ["Banana", 23, 3.14, False]`

## set

- Mutable
  - Once a set is created, you cannot change the items, but you can add or remove items
- Unordered
  - Elements have no defined position
  - You can't access them using an index
- Unique
  - Duplicates are automatically discarded
    - Adding `Apple` twice will result in only one `Apple` appearing in the set

- Creating a set
  - Use curly braces
    - `fruits = {'cherry', 'banana', 'apple'}
  - Use the `for` loop to iterate
    - **Order is not guaranteed**

## tuple

- Ordered
  - Items in list maintain position
- Immutable
  - Cannont be modified after it is created
- Can hold mixed data types
- Duplicate objects are allowed

- Creating Tuples
  - Using parathenses - most common method
    - `my_tuple = (1, "hello", False)`
  - Tuple Packing - paranthenses are optional
    - `my_tuple = 1, "hello", True`
  - Single item tuple - Trailing comma is required
    - `my_tuple = (33,)`

- Accessing items from a Tuple
  - Indexing
    - `my_tuple = (1, "name", False)`
    - `my_tuple[1]` - name
    - `my_tuple[-1]` - False
  - Slicing
    - `my_tuple = (1, "name", False)`
      - `my_tuple[0:2]` - 1 , name
      - `my_tuple[1:]` - name, False

## dictionary

- Uses key-value pairs
  - Each key maps to a value
- Ordered and unique keys
  - Insertion order is maintained
  - Keys must be unique and immutable
    - Strings or numbers
- Values can be any data type
- Mutable
  - Add new key value pairs
  - Update existing values
  - Remove items

- Creating a dictionary
  - `user_data = {"username": "jsmith", "account_type": "Premium", "is_active": True}`
- Accessing an item in a dictionary
  - `print(user_data["username])` - jsmith
- Adding an item to dictionary
  - `user_data["email"] = "jsmith@xyzcorp.com"`
- Updating an item in a dictionary
  - `user_data["account_type"] = "Pro"`
- Removing items from dictionary
  - `del user_data["is_active"]`
- Check for a key
  - `if "username" in user_data`
    - `print("Key exists"`)
