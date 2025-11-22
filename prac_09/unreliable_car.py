"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """Creates a car class that sometimes does not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive, only drives if the car is 'reliable' this time."""
        random_chance = randint(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
