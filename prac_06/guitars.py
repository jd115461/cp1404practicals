"""
CP1404/CP5632 Practical
Guitar program to use the Guitar class created
Expected time: 15 minutes, 48 seconds
Actual time: 20 minutes, 27 seconds
"""
from prac_06.guitar import Guitar


def main():
    """Guitar program using the created Guitar class"""
    guitars = []

    print("My guitars!")
    name = input("Name: ").strip()

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_created_guitar = Guitar(name, year, cost)
        guitars.append(add_created_guitar)
        print(f"{add_created_guitar} added.\n")

        name = input("Name: ").strip()

    # Lines for testing code manually
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


main()
