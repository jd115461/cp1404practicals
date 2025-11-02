"""
CP1404/CP5632 Practical
Guitar program to use the Guitar class created
Expected time: 15 minutes, 48 seconds
Actual time: approx  minutes
"""
from prac_06.guitar import Guitar

def main():
    """Guitar program using the created Guitar class"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        add_created_guitar = Guitar(name, year, cost)
        print(add_created_guitar, "added")
        name = input("Name: ")


