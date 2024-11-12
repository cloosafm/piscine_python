from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def create_baratheon(self):
        """Creates a Baratheon character."""
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
#your code here
    # decorator
    def create_lannister(self, first_name: str, is_alive: bool = True):
        """Creates a Lannister character."""
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''
        Kills the Lannister character.
        '''
        self.is_alive = False