from sys import argv
from ft_filter import ft_filter


def check_input(argv):
    """
    Check the number of arguments.
    Args:
        argv (list): The arguments.
    """
    if len(argv) != 2:
        raise AssertionError("the arguments are bad")


def check_arg1(string) -> list:
    """
    Check that arg1 has only alphanumeric or space characters.
    Args:
        string (str): The string to check.
    Returns:
        list: The list of words from the string.
    """
    if not all(c.isalnum() or c.isspace() for c in string):
        raise AssertionError("the arguments are bad")
    str_list = string.split()
    for item in str_list:
        return [item for item in str_list if item.isalnum()]


def check_arg2(string) -> int:
    """
    Ensure arg2 is cast to int.
    Args:
        string (str): The string to cast to int.
    Returns:
        int: The integer value of the string.
    """
    try:
        number = int(string)
    except ValueError:
        raise AssertionError("the arguments are bad")
    return number


def main(argv):
    """
    Check the input is valid.
    Filter the list of strings based on the length of the words.
    """
    try:
        check_input(argv)
        string_list = check_arg1(argv[0])
        number = check_arg2(argv[1])
    except AssertionError as e:
        print(f"AssertionError: {e}")
    else:
        ft_filtered = list(ft_filter(lambda word: len(word) > number,
                           string_list))
        print("ft_filter result:", ft_filtered)
        og_filtered = list(filter(lambda word: len(word) > number,
                           string_list))
        print("og_filter result:", og_filtered)


if __name__ == "__main__":
    main(argv[1:])
    # print(filter.__doc__)
    # print(ft_filter.__doc__)
