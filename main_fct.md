# Declare a main function in Python 


Let's delve into the various ways to declare and use a main function in Python. The main function serves as the entry point for your program, similar to the main function in languages like C or Java. Here are the common patterns used to declare and use a main function in Python:

## 1. Basic main Function
The simplest way to declare a main function is to define it and call it directly. This approach is straightforward but has limitations when it comes to reusability and modularity.

```python
def main():
    print("Hello, World!")

main()  # Directly calling the main function
```


# 2. Using if __name__ == "__main__":
This is the most common and recommended way to declare a main function in Python. It allows the script to be run directly or imported as a module without executing the main code.

Explanation
__name__: A special built-in variable in Python. When a script is run directly, __name__ is set to "__main__". When a script is imported as a module, __name__ is set to the module's name.
if __name__ == "__main__":: This condition checks if the script is being run directly. If true, it executes the code block inside.
Example

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()  # Only called if the script is run directly
```

## 3. Passing Command-Line Arguments
You can also design your main function to accept command-line arguments using the sys.argv list. This is useful for scripts that need to process input from the command line.

Example

```python
import sys

def main(args):
    print("Arguments:", args)

if __name__ == "__main__":
    main(sys.argv[1:])  # Pass command-line arguments to the main function
```

## 4. Combining with Other Functions
In more complex scripts, you might have multiple functions that are called from within the main function. This helps in organizing the code better.

Example

```python
import sys

def process_data(data):
    print("Processing:", data)

def main(args):
    if len(args) != 1:
        print("Usage: script.py <data>")
        return
    process_data(args[0])

if __name__ == "__main__":
    main(sys.argv[1:])
```


## 5. Using Argument Parsers
For more advanced command-line argument parsing, you can use the argparse module. This provides a more robust way to handle arguments and options.

Example

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some data.")
    parser.add_argument("data", help="The data to process")
    args = parser.parse_args()
    print("Processing:", args.data)

if __name__ == "__main__":
    main()
```


## Summary
- Basic main Function: Simple and direct, but not modular.
- if __name__ == "__main__":: The most common and recommended way, allowing the script to be run directly or imported as a - module.
- Passing Command-Line Arguments: Useful for scripts that need to process input from the command line.
- Combining with Other Functions: Helps in organizing more complex scripts.
- Using Argument Parsers: Provides a robust way to handle command-line arguments and options.

Example with Your Code
Let's apply these concepts to your provided code snippet:

```python
import sys

def NULL_not_found(object: any) -> int:
    print(object)

def main():
    args = sys.argv[1:]  # Skip the script name
    if len(args) != 1:
        print("Usage: script.py <data>")
        return
    NULL_not_found(args[0])

if __name__ == "__main__":
    main()
```


Explanation
- def NULL_not_found(object: any) -> int:: Defines a function that prints the given object.
- def main():: Defines the main function that processes command-line arguments.
- if __name__ == "__main__":: Ensures that the main function is only called if the script is run directly.
- This structure makes your script modular, reusable, and easy to understand.