# Python scripts and programs

## General info
Let's delve into the differences between a Python script and a Python program, what constitutes each of them, and their main use cases.

### Python Script vs. Python Program

#### Python Script
A Python script is a simple, standalone file that contains Python code. It is typically used for small tasks, automation, or quick solutions to specific problems. Scripts are often written to be executed directly from the command line or a terminal.

**Characteristics**:
- **Single File**: A script is usually contained within a single `.py` file.
- **Simplicity**: Scripts are generally simpler and shorter than full-fledged programs.
- **Direct Execution**: Scripts are designed to be executed directly, often without the need for additional setup or configuration.
- **Task-Specific**: Scripts are often written to perform a specific task, such as data processing, file manipulation, or automation.

**Example**:
A script to check if a number is odd or even:
```python
import sys

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise AssertionError("more than one argument is provided")
    try:
        number = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
```

**Use Cases**:
- **Automation**: Automating repetitive tasks, such as file backups or data processing.
- **Quick Solutions**: Solving small problems or performing quick calculations.
- **Prototyping**: Testing out ideas or algorithms before integrating them into larger projects.

**Execute like a shell script**:
- **1. Add a Shebang Line**
Add the following line at the very top of your file:
```python
#!/usr/bin/env python3
```
This line tells the system to use the Python interpreter located in your environment's PATH.
- **2. Make the Script Executable**
Change the file permissions to make the script executable. You can do this using the `chmod +x` command:



#### Python Program
A Python program is a more complex and structured collection of Python code. It often consists of multiple modules, packages, and files, and is designed to solve larger, more complex problems. Programs are typically developed with maintainability, scalability, and reusability in mind.

**Characteristics**:
- **Multiple Files**: A program is usually spread across multiple `.py` files and directories.
- **Complexity**: Programs are more complex and may include various components such as classes, functions, and modules.
- **Modularity**: Programs are designed with modularity in mind, allowing for code reuse and easier maintenance.
- **Configuration**: Programs often require configuration files, dependencies, and setup scripts.

**Example**:
A simple Python program with multiple modules:
```
my_program/
    __init__.py
    main.py
    utils.py
    config.py
```

- `main.py`:
  ```python
  from utils import check_odd_even
  from config import get_number

  def main():
      number = get_number()
      result = check_odd_even(number)
      print(result)

  if __name__ == "__main__":
      main()
  ```

- `utils.py`:
  ```python
  def check_odd_even(number):
      if number % 2 == 0:
          return "I'm Even."
      else:
          return "I'm Odd."
  ```

- `config.py`:
  ```python
  def get_number():
      return 14  # This could be replaced with more complex logic to get the number
  ```

**Use Cases**:
- **Application Development**: Building desktop applications, web applications, or command-line tools.
- **Data Analysis**: Developing complex data analysis pipelines and tools.
- **Machine Learning**: Creating machine learning models and integrating them into larger systems.
- **System Software**: Developing system-level software such as network servers or database management systems.

### Summary
- **Python Script**: A simple, standalone file designed for quick tasks and automation. It is easy to write and execute, making it ideal for small, specific problems.
- **Python Program**: A more complex and structured collection of Python code, designed for larger projects. It emphasizes modularity, maintainability, and scalability, making it suitable for application development and complex problem-solving.

By understanding the differences between Python scripts and programs, you can choose the appropriate approach for your specific needs, whether it's a quick automation task or a large-scale application.





## Single-file code


When the code is contained in a single file, differentiating between a Python script and a Python program can be more nuanced. Here are some key factors to consider:

### Differentiating a Script from a Program in a Single File

#### Python Script
A Python script in a single file is typically characterized by its simplicity and focus on performing a specific task. It is often written for quick execution and may not include complex structures or extensive error handling.

**Characteristics**:
- **Simplicity**: The code is straightforward and easy to understand.
- **Task-Specific**: The script is designed to perform a specific task or solve a particular problem.
- **Minimal Structure**: The script may not include classes or extensive functions.
- **Direct Execution**: The script is intended to be run directly from the command line or terminal.

**Example**:
A script to check if a number is odd or even:
```python
import sys

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise AssertionError("more than one argument is provided")
    try:
        number = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
```

#### Python Program
A Python program in a single file is more complex and structured. It often includes multiple functions, classes, and comprehensive error handling. The program is designed with maintainability, scalability, and reusability in mind.

**Characteristics**:
- **Complexity**: The code includes multiple functions, classes, and possibly modules.
- **Modularity**: The program is designed with modularity in mind, allowing for code reuse and easier maintenance.
- **Extensive Error Handling**: The program includes comprehensive error handling and validation.
- **Configuration and Setup**: The program may include configuration settings and setup code.

**Example**:
A more complex program to check if a number is odd or even, with additional features:
```python
import sys

class NumberChecker:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def is_odd(self):
        return not self.is_even()

def get_number_from_args(args):
    if len(args) != 1:
        raise AssertionError("more than one argument is provided")
    try:
        return int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")

def main():
    args = sys.argv[1:]
    number = get_number_from_args(args)
    checker = NumberChecker(number)
    
    if checker.is_even():
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
```

### Summary
- **Python Script**: Simple, task-specific, minimal structure, and intended for direct execution. It focuses on performing a specific task quickly and efficiently.
- **Python Program**: More complex, modular, includes multiple functions and classes, and designed with maintainability and scalability in mind. It often includes comprehensive error handling and configuration settings.

By considering these factors, you can differentiate between a Python script and a Python program, even when the code is contained in a single file.

