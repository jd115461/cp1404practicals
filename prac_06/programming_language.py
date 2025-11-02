"""
CP1404/CP5632 Practical
Programming Language class code
Estimate: 12 minutes 21 seconds 291 millisecond
Actual: 15 minutes 56 seconds 120 millisecond
"""


class ProgrammingLanguage:
    """Represent info about a Programming Language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of ProgramingLanguage"""
        return f"{self.name}, typing={self.typing}, reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return true if langauge is dynamically typed."""
        return self.typing == "Dynamic"
