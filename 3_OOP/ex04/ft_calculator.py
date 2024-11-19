class calculator:
    """
    Do calculations of 2 vectors.
    The calculations are : dot prodcut, addition, subtraction

    Methods:
        dotproduct(object): Dot product of 2 vectors
        add_vec(object): Add 2 vectors
        sous_vec(object): Subtract 2 vectors
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate dot product of 2 vectors
        """
        dot_product = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {dot_product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add 2 vectors
        """
        add_vector = [float(V1[i]) + float(V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {add_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract 2 vectors
        """
        sous_vector = [float(V1[i]) - float(V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {sous_vector}")

# from ft_calculator import calculator

# a = [5, 10, 2]
# b = [2, 4, 3]
# calculator.dotproduct(a, b)
# calculator.add_vec(a, b)
# calculator.sous_vec(a, b)
