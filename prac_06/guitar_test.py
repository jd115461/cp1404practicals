"""
CP1404/CP5632 Practical
Basic tests for Guitar class code
Expected time: 7.5 minutes
Actual time: approx 5 minutes
"""
from prac_06.guitar import Guitar


def run_tests():
    """Manual tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    guitar_random = Guitar("Another Guitar", 2012, 1512.9)

    expected_age_gibson = 2025 - 1922
    expected_age_random = 2025 - 2012

    print(f"{guitar.name} get_age() - Expected {expected_age_gibson}. Got {guitar.get_age()}")
    print(f"{guitar_random.name} get_age() - Expected {expected_age_random}. Got {guitar_random.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{guitar_random.name} is_vintage() - Expected {False}. Got {guitar_random.is_vintage()}")
    print()


if __name__ == '__main__':
    run_tests()
