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
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''
        Kills the character.
        '''
        pass


class Stark(Character):
    """Inherit from abstract Character class"""
    def die(self):
        '''
        Kills the Stark character.
        '''
        self.is_alive = False
