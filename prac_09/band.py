"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class for storing details of a group of musicians."""

    def __init__(self, name=""):
        """Initialise a Band class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of Band class."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"
