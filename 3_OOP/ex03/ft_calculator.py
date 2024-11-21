class calculator:
    """
    Do calculations of vector with a scalar.
    The calculations are : addition, multiplication, subtraction, division

    Methods:
        __add__(object): Add a scalar to the vector
        __mul__(object): Multiply a scalar to the vector
        __sub__(object): Subtract a scalar from the vector
        __truediv__(object): Divide a scalar from the vector
    """
    def __init__(self, data: list):
        """
        Constructor of the calculator class
        Args:
            data (list): A list of ints or floats
        Raises:
            TypeError: If 'data' is not a list
            TypeError: If 'data' does not contain ints or floats
        """
        if not isinstance(data, list):
            raise TypeError("Please supply a list of ints or floats")
        for i in data:
            if not isinstance(i, (int, float)):
                raise TypeError("The list must include ints or floats only")
        self.data = data

    def __add__(self, object) -> None:
        """
        Add a scalar to the vector
        Args:
            object (int or float): A scalar
        """
        self.data = [i + object for i in self.data]
        print(self.data)

    def __mul__(self, object) -> None:
        """
        Multiply a scalar to the vector
        Args:
            object (int or float): A scalar
        """
        self.data = [i * object for i in self.data]
        print(self.data)

    def __sub__(self, object) -> None:
        """
        Subtract a scalar from the vector
        Args:
            object (int or float): A scalar
        """
        self.data = [i - object for i in self.data]
        print(self.data)

    def __truediv__(self, object) -> None:
        """
        Divide a scalar from the vector
        Args:
            object (int or float): A scalar
        """
        if object == 0:
            raise ValueError("Cannot divide by zero")
        self.data = [i / object for i in self.data]
        print(self.data)
