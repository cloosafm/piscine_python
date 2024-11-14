def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.
    Args:
        limit: int: The limit of the function.
    Returns:
        function: The wrapped function.
    """
    count = 0

    def callLimiter(function):
        """
        Wrapper function.
        Call the limiting function.
        Args:
            function: function: The function to limit.
        Returns:
            function: The called function, if within limits.
        """
        def limit_function(*args: any, **kwds: any):
            """
            Function that returns a given function, within limits.
            If function was called too many times, prints error message.
            Args:
                *args: any: Any number of arguments.
                **kwds: any: Any number of keyword arguments.
            Returns:
                any: The result of the function call.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
