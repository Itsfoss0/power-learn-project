#!/usr/bin/env python3

"""
module to practice oop in python
Create a class Animal that has attributes species
,age, and name. Add a class method oldest_animal()
that returns the oldest animal that has been created
"""


class Animal:
    """Animal Class"""
    _created_animals = []

    def __init__(self, species: str, name: str, age: int) -> None:
        """Constructor"""
        self.name = name
        self.species = species
        self.age = age

        self.__class__._created_animals.append(self)

    def __str__(self) -> str:
        """String representation of the object"""
        return ("{} of Species {}, {} years old".format(
            self.name, self.species, self.age))

    @classmethod
    def oldest_animal(cls) -> object:
        """Lets find the oldest animal shall we"""
        return sorted(cls._created_animals, key=lambda x: x.age)[-1]


if __name__ == "__main__":
    cat = Animal("mammalia", "Amanda", 13)
    dog = Animal("mammalia", "Olivia", 12)
    cow = Animal("mammalia", "Smokie", 25)

    print(Animal.oldest_animal())   # Smokie, which is 25
