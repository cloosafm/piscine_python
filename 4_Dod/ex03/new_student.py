import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class representing a student.
    :param name: The student's name.
    :param surname: The student's surname.
    :param active: The student's status.
    :param login: The student's login.
    :param id: The student's id.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        try:
            self.login = f"{self.name.upper()[0]}{self.surname.lower()}"
        except Exception as e:
            print(f"Error: {e}")
