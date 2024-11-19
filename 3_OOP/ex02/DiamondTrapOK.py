from S1E7 import Baratheon, Lannister


class King(Lannister, Baratheon):
    """Inherit from both Baratheon and Lannister classes
        Create a King character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character. Defaults to True.

        Raises:
            TypeError: If 'first_name' is not a string.
            TypeError: If 'is_alive' is not a boolean.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        King Constructor.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character. Defaults to True.

        Raises:
            TypeError: If 'first_name' is not a string.
            TypeError: If 'is_alive' is not a boolean.
        """
        super(King, self).__init__(first_name, is_alive)

    # getter
    @property
    def eyes(self):
        """
        Return the eye color of the character."""
        return self._eyes

    # setter
    @eyes.setter
    def eyes(self, eyes):
        """
        Set the eye color of the character."""
        if not eyes:
            raise ValueError("Missing 'eyes'")
        if not isinstance(eyes, str):
            raise TypeError("Var 'eyes' must be a str")
        self._eyes = eyes

    # getter
    @property
    def hairs(self):
        """
        Return the hair color of the character."""
        return self._hairs

    # setter
    @hairs.setter
    def hairs(self, hairs):
        """
        Set the hair color of the character."""
        if not hairs:
            raise ValueError("Missing 'hairs'")
        if not isinstance(hairs, str):
            raise TypeError("Var 'hairs' must be a str")
        self._hairs = hairs

    def die(self):  # need to keep it, as it is in the base class
        """
        Kill the Baratheon character
        Set their is_alive status to False.
        """
        self.is_alive = False
