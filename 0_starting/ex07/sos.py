from sys import argv


NESTED_MORSE = {
                " ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "0": "----- ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ",
}


def convert_to_morse(text) -> str:
    """
    Convert a string to morse code.
    Args:
        text (str): The string to convert.
    Returns:
        str: The string converted to morse code.
    """
    text = text.upper()
    for key, value in NESTED_MORSE.items():
        text = text.replace(key, value)
    text = text.rstrip()
    return text


def main(argv):
    """
    Check the input is valid.
    Print the input converted to morse code.
    """
    try:
        if len(argv) != 1:
            raise AssertionError("the arguments are bad")
        if not all(c.isalnum() or c.isspace() for c in argv[0]):
            raise AssertionError("the arguments are bad")
        morse = convert_to_morse(argv[0])
        print(morse)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(argv[1:])
