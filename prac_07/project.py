"""
CP1404/CP5632 Practical

"""
from datetime import date


class Project:
    """Project class for storing details of a project."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion_percentage >= 100
