# Read, Write and Manage Files

- Opening files
  - Always close file after use
    - You can use the `with` statement to handle this automatically
  - Syntax
    - `file_object = with open(filename, mode)`
  


- Modes
  - `r`
    - Default mode
    - Opens the file to be read
    - Throws error if file doesn't exist

- `w`
  - Creates a new file or overwrites existing content

- `a`
  - Adds new content to the end of the file without removing existing data