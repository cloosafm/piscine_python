from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        Baratheon Constructor.
        Initialize character with following args:
            - first name
            - (optional) is_alive status.
        '''
        super().__init__(first_name, is_alive, "Baratheon", "brown", "dark")

    def die(self):  # need to keep it as it is in the base class
        '''
        Kills the Baratheon character.
        '''
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        Lannister Constructor.
        Initialize character with following args:
            - first name
            - (optional) is_alive status.
        '''
        super().__init__(first_name, is_alive, "Lannister", "blue", "light")

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creates a Lannister character."""
        return cls(first_name, is_alive)

    def die(self):  # need to keep it as it is in the base class
        '''
        Kills the Lannister character.
        '''
        self.is_alive = False
