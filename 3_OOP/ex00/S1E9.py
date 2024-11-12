from abc import ABC, abstractmethod


class Character(ABC):
    """
        Abstract class
        Args:
            first_name (str): The first name of the character.
    		is_alive (bool): The status of the character.
                optional, defaults to True.
    """
    # @abstractmethod
    #your code here
    def __init__(self, first_name, is_alive=True):
        '''
        Initializes character with first name and optional is_alive status.
        '''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''
        Kills the character.
        '''
        self.is_alive = False

class Stark(Character):
    """Inherit from abstract Character class"""
    #your code here
