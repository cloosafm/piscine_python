def square(x: int | float) -> int | float:
    """Return the square of the input.
        Args:
            x: int or float
        Returns:
            int or float
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    return x * x


def pow(x: int | float) -> int | float:
    """Return the exponentiation of the input.
        Args:
            x: int or float
        Returns:
            int or float
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Function that takes as argument a number and a function
    Return an object that will return the result of the arguments calculation.
    Args:
        x: int or float
        function: a function
    Returns:
        an object
    """
    count = 0

    def inner() -> float:
        nonlocal count
        res = function(x)
        for i in range(count):
            res = function(res)
        count += 1
        return res
    return inner
