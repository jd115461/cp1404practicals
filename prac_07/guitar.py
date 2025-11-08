"""
CP1404/CP5632 Practical
Guitar class from prac 6
"""
from datetime import date

VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the current age of a guitar."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage or not based on if it's older than 50 years old."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars by their year so they can be sorted."""
        return self.year < other.year