# 📘 Assignment: Functions, Modules, and File I/O

## 🎯 Objective

Practice defining reusable functions, organizing code into modules, and using file input/output in Python.

## 📝 Tasks

### 🛠️ Build Reusable Functions

#### Description
Create helper functions that perform arithmetic and text processing, then use them from the main program.

#### Requirements
Completed program should:

- Define `add_numbers(a, b)` to return the sum of two values.
- Define `format_greeting(name)` to return a personalized greeting string.
- Define `count_words(text)` to return the number of words in a string.
- Call these functions from the main program.

### 🛠️ Organize Code into a Module

#### Description
Move helper functions into a separate module file and import that module into the main script.

#### Requirements
Completed program should:

- Create a module file named `file_utils.py`.
- Import the helper functions from `file_utils.py` in `starter-code.py`.
- Use at least one imported function in `starter-code.py`.

### 🛠️ Read from and Write to Files

#### Description
Read text from a file, process the content, and write the results to a new output file.

#### Requirements
Completed program should:

- Read from `input.txt` or another text file.
- Count words in the file content using `count_words()`.
- Write the result to `output.txt`.
- Handle a missing input file with a clear error message.
- Example output written to `output.txt`:
  ```text
  Word count: 42
  ```
