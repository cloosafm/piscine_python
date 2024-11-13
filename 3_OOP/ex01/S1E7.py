from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Baratheon Constructor.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character. Defaults to True.

        Raises:
            TypeError: If 'first_name' is not a string.
            TypeError: If 'is_alive' is not a boolean.
        """
        super().__init__(first_name, is_alive, "Baratheon", "brown", "dark")

    def __str__(self):
        """
        Return a user-friendly string representation of the character.
        """
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def __repr__(self):
        """
        Return the official string representation of the Baratheon character.
        """
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def die(self):  # need to keep it, as it is in the base class
        """
        Kill the Baratheon character
        Set their is_alive status to False.
        """
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Lannister Constructor.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character. Defaults to True.

        Raises:
            TypeError: If 'first_name' is not a string.
            TypeError: If 'is_alive' is not a boolean.
        """
        super().__init__(first_name, is_alive, "Lannister", "blue", "light")

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creates a Lannister character."""
        return cls(first_name, is_alive)

    def __str__(self):
        """
        Return a user-friendly string representation of the Lann. character.
        """
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def __repr__(self):
        """
        Return the official string representation of the Lann. character.
        """
        return f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"

    def die(self):  # need to keep it, as it is in the base class
        """
        Kill the Lannister character
        Set their is_alive status to False.
        """
        self.is_alive = False
