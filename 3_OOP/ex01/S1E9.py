from abc import ABC, abstractmethod


class Character(ABC):
    """
        Abstract class
        Args:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character.
                optional, defaults to True.
    """

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
        Kill the character.
        '''
        pass
        # ```pass``` not actually needed, as it's an abstract method

    # getter
    @property
    def first_name(self):
        '''
        Return the first name of the character.
        '''
        return self.first_name

    # setter
    @first_name.setter
    def first_name(self, first_name):
        '''
        Set the first name of the character.
        '''
        # add error mngmt
        self.first_name = first_name

    # getter
    @property
    def is_alive(self):
        '''
        Return the status of the character.
        '''
        return self.is_alive

    # setter
    @is_alive.setter
    def is_alive(self, is_alive):
        '''
        Set the character alive or dead.
        '''
        # add error mngmt
        self.is_alive = is_alive


class Stark(Character):
    """Inherit from abstract Character class"""
    def die(self):
        '''
        Kills the Stark character.
        '''
        self.is_alive = False
