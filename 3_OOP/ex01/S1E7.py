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
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    # getter
    @property
    def eyes(self):
        '''
        Return the eye color of the character.
        '''
        return self._eyes

    # setter
    @eyes.setter
    def eyes(self, eyes):
        '''
        Set the eye color of the character.
        '''
        if not eyes:
            raise ValueError("Missing 'eyes'")
        if not isinstance(eyes, str):
            raise TypeError("Var 'eyes' must be a str")
        self._eyes = eyes

    # getter
    @property
    def hairs(self):
        '''
        Return the hair color of the character.
        '''
        return self._hairs

    # setter
    @hairs.setter
    def hairs(self, hairs):
        '''
        Set the hair color of the character.
        '''
        if not hairs:
            raise ValueError("Missing 'hairs'")
        if not isinstance(hairs, str):
            raise TypeError("Var 'hairs' must be a str")
        self._hairs = hairs

    def die(self):  # need to keep it as it is in the base class
        '''
        Kills the Baratheon character.
        '''
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        '''
        Constructor.
        Initialize character with following args:
            - first name
            - (optional) is_alive status.
        '''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creates a Lannister character."""
        return cls(first_name, is_alive)

    # getter
    @property
    def family_name(self):
        '''
        Return the family name of the character.
        '''
        return self._family_name

    # setter
    @family_name.setter
    def family_name(self, family_name):
        '''
        Set the family name of the character.
        '''
        if not isinstance(family_name, str):
            raise TypeError("Var 'family_name' must be a str")
        self._family_name = family_name

    # getter
    @property
    def eyes(self):
        '''
        Return the eye color of the character.
        '''
        return self._eyes

    # setter
    @eyes.setter
    def eyes(self, eyes):
        '''
        Set the eye color of the character.
        '''
        if not eyes:
            raise ValueError("Missing 'eyes'")
        if not isinstance(eyes, str):
            raise TypeError("Var 'eyes' must be a str")
        self._eyes = eyes

    # getter
    @property
    def hairs(self):
        '''
        Return the hair color of the character.
        '''
        return self._hairs

    # setter
    @hairs.setter
    def hairs(self, hairs):
        '''
        Set the hair color of the character.
        '''
        if not hairs:
            raise ValueError("Missing 'hairs'")
        if not isinstance(hairs, str):
            raise TypeError("Var 'hairs' must be a str")
        self._hairs = hairs

    def die(self):  # need to keep it as it is in the base class
        '''
        Kills the Lannister character.
        '''
        self.is_alive = False
