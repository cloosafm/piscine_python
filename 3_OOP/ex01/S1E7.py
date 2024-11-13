from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        Constructor.
        Initialize character with following args:
            - first name
            - (optional) is_alive status.
        '''
        # self.first_name = first_name
        # self.is_alive = is_alive
        self.create_baratheon(first_name, is_alive)

    def create_baratheon(self, first_name: str, is_alive: bool = True):
        """Creates a Baratheon character."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        '''
        Kills the Baratheon character.
        '''
        self.is_alive = False


class Lannister(Character):
    """Inherit from abstract Character class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        Constructor.
        Initialize character with following args:
            - first name
            - (optional) is_alive status.
        '''
        self.create_lannister(first_name, is_alive)

    def create_lannister(self, first_name: str, is_alive: bool = True):
        """Creates a Lannister character."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''
        Kills the Lannister character.
        '''
        self.is_alive = False