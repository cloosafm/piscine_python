import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.id = id: str = field(default_factory = generate_id)
