from abc import ABC, abstractmethod


class Character(ABC):
    """
        Abstract class
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character.
                optional, defaults to True.
    """

# add error magmt, checks for attribute types
    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        Constructor.
        Initialize character with following args:
            - first name
            - (optional) is_alive status.
        '''
        if not isinstance(first_name, str):
            raise TypeError("Var 'first_name' must be a str")
        if not isinstance(is_alive, bool):
            raise TypeError("Var 'is_alive' must be a bool")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''
        Kills the character.
        '''
        pass
        # ```pass``` not actually needed, as it's an abstract method


class Stark(Character):
    """Inherit from abstract Character class"""
    def die(self):
        '''
        Kills the Stark character.
        '''
        self.is_alive = False
