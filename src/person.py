from dataclasses import dataclass

# We set this an immutable because we put them in a set
@dataclass(frozen = True)
class Person:
    """Class for tracking a person making a bus journey"""
    name: str
    age: int
