from abc import ABC, abstractmethod


class Character(ABC):
    """
        Abstract class
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character.
                optional, defaults to True.
        Methods:
            die(): abstract method to kill the character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor to initialize a Character.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character. Defaults to True.
        Raises:
            TypeError: If 'first_name' is not a string.
            TypeError: If 'is_alive' is not a boolean.
        """
        if not isinstance(first_name, str):
            raise TypeError("Var 'first_name' must be a str")
        if not isinstance(is_alive, bool):
            raise TypeError("Var 'is_alive' must be a bool")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to kill the character."""
        pass
        # ```pass``` not actually needed, as it's an abstract method

    # getters and setters:
    #  method and vars can't have same name : prepend an '_' to var name
    #  -> getter will return self._<var> instead of self.<var>
    #  -> setter will set 'self._<var> = <var>' instead of 'self.<var> = <var>'

    # getter
    @property
    def first_name(self):
        """
        Return the first name of the character."""
        return self._first_name

    # setter
    @first_name.setter
    def first_name(self, first_name):
        """
        Set the first name of the character."""
        if not first_name:
            raise ValueError("Missing 'first_name'")
        if not isinstance(first_name, str):
            raise TypeError("Var 'first_name' must be a str")
        self._first_name = first_name

    # getter
    @property
    def is_alive(self):
        """
        Return the status of the character."""
        return self._is_alive

    # setter
    @is_alive.setter
    def is_alive(self, is_alive):
        """
        Set the character alive or dead."""
        if not isinstance(is_alive, bool):
            raise TypeError("Var 'is_alive' must be a bool")
        self._is_alive = is_alive


class Stark(Character):
    """Inherit from abstract Character class
        Create a Stark character.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The status of the character. Defaults to True.

    Methods:
        die(): Kills the character by setting their is_alive status to False.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Stark Constructor.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character. Defaults to True.

        Raises:
            TypeError: If 'first_name' is not a string.
            TypeError: If 'is_alive' is not a boolean.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Kill the Stark character by setting their is_alive status to False."""
        self.is_alive = False
