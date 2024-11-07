#!/usr/bin/env python3
from sys import argv

"""
if using 'assert' keyword, program will NOT stop if condition is false
'assert' is not error-handling !!! more like a debugging tool
    -> not supposed to be used with try/except
also, if used as is, will print all the Traceback msg
'assert' usage (msg is optional) :
    assert len(argv) == 1, "more than one argument is provided"
"""


def main(argv):
    if not argv:
        return
    try:
        if len(argv) > 1:
            raise AssertionError("more than one argument is provided")
        number = int(argv[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    else:
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")


if __name__ == "__main__":
    main(argv[1:])
