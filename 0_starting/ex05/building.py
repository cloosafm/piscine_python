from sys import argv, stdin

"""
This programs displays stats about the input string.
It will accept only one string as an argument.
If no argument is provided, the user will be prompted to provide one.
It will display the sum of its:
- upper-case characters
- lower-case characters
- punctuation characters
- digits
- spaces
"""


def check_for_input(argv) -> str:
    if not argv:
        print("Please provide a string:")
        line = stdin.readline()
        return line
    if len(argv) > 1:
        raise AssertionError("more than one argument is provided")
    return argv[0]


def ft_ispunct(char) -> bool:
    """
    Check if a character is a punctuation character.
    Args:
        char (str): The character to check.
    Returns:
        bool: True if the character is a punctuation mark, False otherwise.

    Below is a listing of punctuation characters to create our set:
    https://www.yourdictionary.com/articles/english-punctuation-marks

    non-ascii punctuation characters with unicode:
        U+2013	em dash
        U+2014	en dash
        U+2018	left single quotation marks
        U+2019	right single quotation marks
        U+2026	ellipsis

    """
    punct_set = {".", "?", "!", ",", ";", ":", "–", "—", "-",
                 "(", ")", "[", "]", "{", "}", "'", "\"", "‘", "’", "…"}
    return char in punct_set
    # if char in punct_set:
    #     return True


def string_stats(user_input) -> None:
    """
    Print statistics about the input string.

    Args:
        user_input (str): The input string.
    """
    print("The text contains", len(user_input), "characters:")
    print(sum(1 for c in user_input if c.isupper()), "upper letters")
    print(sum(1 for c in user_input if c.islower()), "lower letters")
    print(sum(1 for c in user_input if ft_ispunct(c)), "punctuation marks")
    print(sum(1 for c in user_input if c.isspace()), "spaces")
    print(sum(1 for c in user_input if c.isdigit()), "digits")


def main(argv):
    try:
        user_input = check_for_input(argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    else:
        string_stats(user_input)



if __name__ == "__main__":
    main(argv[1:])
