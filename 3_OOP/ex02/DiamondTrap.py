from S1E7 import Baratheon, Lannister

#  need to check @ 42 the order of the classes
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

    def get_eyes(self):
        """Bad practice way to do a getter,
                can't use @property because name is not that of the attribute
            Return the eye color of the character.
        """
        return self.eyes

    def set_eyes(self, eyes):
        """Bad practice way to do a setter
            can't use @<var_name>.setter because (see getter issue)
            Set the eye color of the character.
        """
        self.eyes = eyes

    def get_hairs(self):
        """Bad practice way to do a getter,
                can't use @property because name is not that of the attribute
            Return the hair color of the character.
        """
        return self.hairs

    def set_hairs(self, hairs):
        """Bad practice way to do a setter
            can't use @<var_name>.setter because (see getter issue)
            Set the hair color of the character.
        """
        self.hairs = hairs

    def die(self):  # need to keep it, as it is in the base class
        """
        Kill the Baratheon character
        Set their is_alive status to False.
        """
        self.is_alive = False
